/* ==========================================================================
   Lernschleife aus den Instagram-Statistiken.

   Liest je Beitrag Reichweite, Speicherungen, Teilungen, Likes, Kommentare
   (bei Reels: Aufrufe) und das Konto (Follower, Reichweite, Online-Zeiten
   der Follower). Daraus entsteht state/strategie.json:
     - formatGewicht:  welche Formate überdurchschnittlich laufen
     - fachGewicht:    welche Fächer
     - hookGewicht:    welche Aufhänger-Typen (frage, fehler, zahl, aussage)
     - besteStunden:   drei Uhrzeiten, zu denen die Follower online sind
   Der Planer und der Autor lesen diese Gewichte; ohne Daten bleibt alles
   beim Standard. Berechtigung: instagram_business_manage_insights.
   ========================================================================== */

import { CONFIG } from "./config.mjs";
import { hhmm } from "./zeit.mjs";

const METRIKEN_BILD = "reach,saved,shares,likes,comments,total_interactions";
const METRIKEN_REEL = "reach,saved,shares,likes,comments,total_interactions,views";
const METRIKEN_REEL_WATCH = "ig_reels_avg_watch_time,ig_reels_video_view_total_time";
const METRIK_REEL_SKIP = "reels_skip_rate";
/* Wachstumskennzahlen: neue Follower und Profilbesuche je Beitrag – nicht jede
   API-Version liefert sie, deshalb mit Rückfall auf die Grundmetriken. */
const METRIKEN_WACHSTUM = "follows,profile_visits";

/* Stories haben einen eigenen Metriksatz. Anders als Feed/Reels sind ihre
   Insights nur kurz verfuegbar; deshalb werden sie durch den stuendlichen
   Lauf separat eingesammelt und dauerhaft ins Ledger geschrieben. */
const METRIKEN_STORY_KERN = "reach,views,shares,total_interactions";
const METRIKEN_STORY_AKTION = "replies,follows,profile_visits,profile_activity";
const STORY_INSIGHTS_MIN_ALTER_STUNDEN = 1;
const STORY_INSIGHTS_MAX_ALTER_STUNDEN = 23.75;
const STORY_INSIGHTS_ABSTAND_STUNDEN = 4;
const STORY_INSIGHTS_ENDSPURT_ABSTAND_STUNDEN = 2;

/* Dashboard-Snapshots: Feed/Reels werden in den ersten sieben Tagen mehrfach
   gemessen. So bleibt nicht nur der Endstand erhalten, sondern auch die
   Wachstumskurve eines Inhalts. Das separate JSON ist absichtlich kompakt und
   wird vom Dashboard direkt aus dem Asset-Zweig gelesen. */
const SNAPSHOT_MIN_ALTER_STUNDEN = 0.75;
const SNAPSHOT_MAX_ALTER_STUNDEN = 168.5;
const SNAPSHOT_MAX_PRO_MEDIUM = 24;
const SNAPSHOT_MAX_KONTO = 1500;

function werte(r) {
  const o = {};
  for (const m of r.data || []) o[m.name] = m.values?.[0]?.value ?? m.total_value?.value ?? 0;
  return o;
}

/* Kennzahlen eines Mediums (Fehler → null, z. B. fehlende Berechtigung). */
export async function medienInsights(ig, medium) {
  const istReel = medium.media_type === "VIDEO" || medium.media_product_type === "REELS";
  const basis = istReel ? METRIKEN_REEL : METRIKEN_BILD;
  try {
    let out;
    try {
      out = werte(await ig.anfrage("GET", `${medium.id}/insights`, { metric: `${basis},${METRIKEN_WACHSTUM}` }, { versuche: 1 }));
    } catch {
      out = werte(await ig.anfrage("GET", `${medium.id}/insights`, { metric: basis }));
    }
    /* Instagram nennt neben Sends/Likes auch Watch Time als zentrales
       Rankingsignal. Die Reel-Watch-Metriken werden separat abgefragt:
       Falls ein Konto/API-Stand sie nicht liefert, verlieren wir dadurch
       nicht die robusten Basis-Insights. */
    if (istReel) {
      try { Object.assign(out, werte(await ig.anfrage("GET", `${medium.id}/insights`, { metric: METRIKEN_REEL_WATCH }, { versuche: 1 }))); }
      catch { /* optionale Metrik, Basiswerte bleiben */ }
      /* Meta liefert die Skip-Rate nicht auf jedem Konto/API-Stand. Deshalb
         separat: Ein unbekanntes Feld darf die Watch-Time nicht mitreißen. */
      try { Object.assign(out, werte(await ig.anfrage("GET", `${medium.id}/insights`, { metric: METRIK_REEL_SKIP }, { versuche: 1 }))); }
      catch { /* optional */ }
    }
    return out;
  } catch {
    return null;
  }
}


/* Story-Navigation kommt als Breakdown statt als normale Zahl. Den Gesamtwert
   behalten wir und legen die einzelnen Aktionen daneben ab, sofern Meta sie
   liefert (z. B. taps_forward, taps_back, exits, swipe_forward). */
function storyNavigationWerte(r) {
  const out = werte(r);
  const m = (r.data || []).find((x) => x.name === "navigation");
  const breakdowns = m?.total_value?.breakdowns || m?.values?.[0]?.value?.breakdowns || [];
  const results = breakdowns.flatMap((b) => b?.results || []);
  let summe = 0, gefunden = 0;
  for (const x of results) {
    const roh = x?.dimension_values?.[0] ?? x?.dimension_value ?? x?.name ?? null;
    if (!roh) continue;
    const wert = Number(x?.value) || 0;
    const schluessel = `navigation_${String(roh).toLowerCase().replace(/^story_/, "").replace(/[^a-z0-9]+/g, "_")}`;
    out[schluessel] = wert;
    summe += wert;
    gefunden++;
  }
  if (gefunden && !(Number(out.navigation) > 0)) out.navigation = summe;
  return out;
}

/* Kennzahlen einer Story. Metriken werden in kleinen Gruppen und bei Bedarf
   einzeln abgefragt: Ein Feld, das auf einer API-Version nicht verfuegbar ist,
   darf nicht verhindern, dass die uebrigen Story-Daten gespeichert werden. */
export async function storyInsights(ig, storyId) {
  if (!storyId) return null;
  const out = {};
  const sammeln = async (metric) => {
    try {
      Object.assign(out, werte(await ig.anfrage("GET", `${storyId}/insights`, { metric }, { versuche: 1 })));
      return true;
    } catch {
      return false;
    }
  };

  for (const gruppe of [METRIKEN_STORY_KERN, METRIKEN_STORY_AKTION]) {
    if (!(await sammeln(gruppe))) {
      for (const metric of gruppe.split(",")) await sammeln(metric);
    }
  }

  try {
    Object.assign(out, storyNavigationWerte(await ig.anfrage(
      "GET", `${storyId}/insights`,
      { metric: "navigation", breakdown: "story_navigation_action_type" },
      { versuche: 1 },
    )));
  } catch { /* optional; Kernmetriken bleiben */ }

  /* Seit 2026 liefert Meta Link-Klicks fuer Stories nur ueber Facebook-Login.
     Bei Instagram-Login wird die Abfrage bewusst ausgelassen. */
  if (ig.host === "facebook") await sammeln("link_clicks");

  return Object.keys(out).length ? out : null;
}

/* Story-Insights muessen eingesammelt werden, solange die Story noch lebt.
   Der Bot laeuft stuendlich, misst aber nicht bei jedem Lauf: normal alle vier
   Stunden, in den letzten Stunden vor Ablauf alle zwei. So bleibt der letzte
   gespeicherte Stand nah am 24-h-Endwert, ohne die API unnoetig zu belasten. */
export async function storyInsightsAktualisieren(ig, ledger, {
  log = console.log,
  jetzt = new Date(),
  mindestAlterStunden = STORY_INSIGHTS_MIN_ALTER_STUNDEN,
  maxAlterStunden = STORY_INSIGHTS_MAX_ALTER_STUNDEN,
  abstandStunden = STORY_INSIGHTS_ABSTAND_STUNDEN,
  endspurtAbstandStunden = STORY_INSIGHTS_ENDSPURT_ABSTAND_STUNDEN,
  snapshots = null,
} = {}) {
  const jetztDatum = jetzt instanceof Date ? jetzt : new Date(jetzt);
  const jetztMs = jetztDatum.getTime();
  if (!Number.isFinite(jetztMs)) throw new Error("Ungueltiger Zeitpunkt fuer Story-Insights");

  const stories = (ledger.veroeffentlicht || []).filter((e) =>
    e.art === "story" && e.medienId && e.medienId !== "trocken");
  let gemessen = 0, versucht = 0;

  for (const e of stories) {
    const veroeffentlichtMs = new Date(e.veroeffentlicht || `${e.datum}T12:00:00Z`).getTime();
    if (!Number.isFinite(veroeffentlichtMs)) continue;
    const alterStunden = (jetztMs - veroeffentlichtMs) / 3600000;
    if (alterStunden < mindestAlterStunden || alterStunden >= maxAlterStunden) continue;

    const letzterMs = e.insightsStand ? new Date(e.insightsStand).getTime() : NaN;
    const noetigerAbstand = alterStunden >= 20 ? endspurtAbstandStunden : abstandStunden;
    if (Number.isFinite(letzterMs) && (jetztMs - letzterMs) / 3600000 < noetigerAbstand) continue;

    versucht++;
    const m = await storyInsights(ig, e.medienId);
    if (!m) continue;
    e.insights = m;
    e.insightsStand = jetztDatum.toISOString();
    e.insightsAlterStunden = Math.round(alterStunden * 10) / 10;
    if (snapshots) snapshotHinzufuegen(snapshots, e, m, alterStunden, e.insightsStand);
    gemessen++;
  }

  if (versucht) log(`Story-Insights: ${gemessen}/${versucht} Storys gespeichert`);
  return { gemessen, versucht };
}

/* --------------------------------------------------------------------------
   Zeitreihen fuer das Dashboard
   -------------------------------------------------------------------------- */

function snapshotAbstandStunden(alterStunden) {
  if (alterStunden < 6) return 1.5;
  if (alterStunden < 24) return 3;
  if (alterStunden < 72) return 8;
  return 24;
}

function snapshotMetriken(m = {}) {
  const out = {};
  for (const [k, v] of Object.entries(m)) {
    if (typeof v === "number" && Number.isFinite(v)) out[k] = v;
  }
  return out;
}

function snapshotFaellig(bestand, e, alterStunden, jetztMs) {
  const liste = bestand?.medien?.[String(e.medienId)]?.snapshots || [];
  if (!liste.length) return true;
  const letzterMs = Date.parse(liste.at(-1)?.stand || "");
  if (!Number.isFinite(letzterMs)) return true;
  return (jetztMs - letzterMs) / 3600000 >= snapshotAbstandStunden(alterStunden);
}

export function snapshotHinzufuegen(bestand, e, metriken, alterStunden, stand = new Date().toISOString()) {
  if (!bestand || !e?.medienId || !metriken) return bestand;
  bestand.version = 1;
  bestand.medien ||= {};
  const id = String(e.medienId);
  const alt = bestand.medien[id] || {};
  const meta = {
    art: e.art || null,
    datum: e.datum || null,
    titel: e.titel || null,
    format: e.format || null,
    fach: e.fach || null,
    hook: e.hookTyp || e.hookMuster || null,
    dauer: Number(e.dauer) || null,
    veroeffentlicht: e.veroeffentlicht || null,
  };
  const snapshots = [...(alt.snapshots || []), {
    stand,
    alterStunden: Math.round(Number(alterStunden) * 10) / 10,
    ...snapshotMetriken(metriken),
  }].slice(-SNAPSHOT_MAX_PRO_MEDIUM);
  bestand.medien[id] = { ...alt, ...meta, snapshots };
  bestand.stand = stand;

  /* Alte Medien entfernen, damit die State-Datei auch nach Monaten klein
     bleibt. 120 Tage reichen fuer Dashboard und Langzeitvergleich; die
     Tagesaggregate bleiben separat erhalten. */
  const grenze = Date.now() - 120 * 86400000;
  for (const [mediumId, eintrag] of Object.entries(bestand.medien)) {
    const t = Date.parse(eintrag.veroeffentlicht || `${eintrag.datum || ""}T12:00:00Z`);
    if (Number.isFinite(t) && t < grenze) delete bestand.medien[mediumId];
  }
  return bestand;
}

/* Feed/Reels: in den ersten sieben Tagen eine echte Wachstumskurve aufbauen.
   Bestehende alte Posts werden nicht kuenstlich rueckdatiert; beim ersten Lauf
   entsteht einfach der erste Snapshot mit seinem tatsaechlichen Alter. */
export async function medienSnapshotsAktualisieren(ig, ledger, snapshots, {
  log = console.log,
  jetzt = new Date(),
  maxProLauf = 8,
} = {}) {
  const jetztDatum = jetzt instanceof Date ? jetzt : new Date(jetzt);
  const jetztMs = jetztDatum.getTime();
  if (!Number.isFinite(jetztMs)) throw new Error("Ungueltiger Zeitpunkt fuer Medien-Snapshots");
  snapshots ||= { version: 1, medien: {}, konto: [] };
  snapshots.medien ||= {};

  const kandidaten = (ledger.veroeffentlicht || []).filter((e) => {
    if (e.art !== "beitrag" || !e.medienId || e.medienId === "trocken") return false;
    const veroeffentlichtMs = Date.parse(e.veroeffentlicht || `${e.datum}T12:00:00Z`);
    if (!Number.isFinite(veroeffentlichtMs)) return false;
    const alter = (jetztMs - veroeffentlichtMs) / 3600000;
    return alter >= SNAPSHOT_MIN_ALTER_STUNDEN
      && alter <= SNAPSHOT_MAX_ALTER_STUNDEN
      && snapshotFaellig(snapshots, e, alter, jetztMs);
  }).slice(0, Math.max(1, Number(maxProLauf) || 8));

  if (!kandidaten.length) return { gemessen: 0, versucht: 0 };

  const medienTypen = new Map();
  try {
    const liste = await ig.anfrage("GET", `${ig.kontoId}/media`, { fields: "id,media_type,media_product_type,timestamp", limit: 60 });
    for (const m of liste.data || []) medienTypen.set(String(m.id), m);
  } catch { /* Fallback ueber Ledger-Format */ }

  let gemessen = 0;
  for (const e of kandidaten) {
    const veroeffentlichtMs = Date.parse(e.veroeffentlicht || `${e.datum}T12:00:00Z`);
    const alterStunden = (jetztMs - veroeffentlichtMs) / 3600000;
    const medium = medienTypen.get(String(e.medienId))
      || { id: e.medienId, media_type: e.format === "reel" ? "VIDEO" : "CAROUSEL_ALBUM", media_product_type: e.format === "reel" ? "REELS" : undefined };
    const m = await medienInsights(ig, medium);
    if (!m) continue;
    e.insights = m;
    e.insightsStand = jetztDatum.toISOString();
    e.insightsAlterStunden = Math.round(alterStunden * 10) / 10;
    snapshotHinzufuegen(snapshots, e, m, alterStunden, e.insightsStand);
    gemessen++;
  }

  if (kandidaten.length) log(`Medien-Snapshots: ${gemessen}/${kandidaten.length} Feed/Reels gespeichert`);
  return { gemessen, versucht: kandidaten.length };
}

/* Ein leichter Konto-Snapshot pro Stundenlauf. Damit kann das Dashboard auch
   intraday einen Follower-Verlauf zeigen, ohne die schwere Lernschleife
   stuendlich auszufuehren. */
export async function kontoSnapshotAktualisieren(ig, snapshots, {
  log = console.log,
  jetzt = new Date(),
  minAbstandStunden = 0.8,
} = {}) {
  const jetztDatum = jetzt instanceof Date ? jetzt : new Date(jetzt);
  const jetztMs = jetztDatum.getTime();
  if (!Number.isFinite(jetztMs)) throw new Error("Ungueltiger Zeitpunkt fuer Konto-Snapshot");
  snapshots ||= { version: 1, medien: {}, konto: [] };
  snapshots.konto ||= [];
  const letzterMs = Date.parse(snapshots.konto.at(-1)?.stand || "");
  if (Number.isFinite(letzterMs) && (jetztMs - letzterMs) / 3600000 < minAbstandStunden) {
    return { gemessen: 0, versucht: 0 };
  }
  try {
    const k = await ig.anfrage("GET", ig.kontoId, { fields: "followers_count,media_count" }, { versuche: 1 });
    snapshots.konto.push({
      stand: jetztDatum.toISOString(),
      follower: Number(k.followers_count) || 0,
      medien: Number(k.media_count) || 0,
    });
    snapshots.konto = snapshots.konto.slice(-SNAPSHOT_MAX_KONTO);
    snapshots.stand = jetztDatum.toISOString();
    log(`Konto-Snapshot: ${Number(k.followers_count) || 0} Follower`);
    return { gemessen: 1, versucht: 1 };
  } catch {
    return { gemessen: 0, versucht: 1 };
  }
}

/* Konto: Follower, Reichweite der letzten 7 Tage, Online-Stunden. */
export async function kontoInsights(ig) {
  const out = { follower: null, reichweite7: null, onlineStunden: null };
  try { out.follower = (await ig.anfrage("GET", ig.kontoId, { fields: "followers_count,media_count" })).followers_count; } catch { /* egal */ }
  try { const p = await ig.anfrage("GET", ig.kontoId, { fields: "biography,website,profile_picture_url,name" }, { versuche: 1 }); out.profil = { bio: p.biography || "", website: p.website || "", bild: !!p.profile_picture_url, name: p.name || "" }; } catch { /* egal */ }
  try {
    const r = await ig.anfrage("GET", `${ig.kontoId}/insights`, { metric: "reach", period: "day", metric_type: "total_value", since: Math.floor(Date.now() / 1000) - 7 * 86400, until: Math.floor(Date.now() / 1000) });
    out.reichweite7 = r.data?.[0]?.total_value?.value ?? r.data?.[0]?.values?.reduce((a, v) => a + (v.value || 0), 0) ?? null;
  } catch { /* egal */ }
  try {
    const r = await ig.anfrage("GET", `${ig.kontoId}/insights`, { metric: "online_followers", period: "lifetime" });
    const v = r.data?.[0]?.values?.[0]?.value;
    if (v && typeof v === "object") out.onlineStunden = v;   // { "0": n, "1": n, … } in UTC
  } catch { /* egal */ }
  return out;
}

/* Bewertung eines Beitrags: Speichern und Teilen zählen am meisten. */
export function punkte(m) {
  if (!m) return null;
  /* Neue Follower aus einem Beitrag sind das eigentliche Ziel und zählen am stärksten. */
  return (m.follows || 0) * 10 + (m.profile_visits || 0) + (m.saved || 0) * 3 + (m.shares || 0) * 4 + (m.comments || 0) * 2 + (m.likes || 0) + (m.reach || 0) / 100 + (m.views || 0) / 300;
}

/* Hook-Lernen darf nicht bloss den Hook belohnen, der zufaellig schon mehr
   Reichweite bekam. Fuer neue Zielgruppen ist Teilen/Senden pro Reach das
   wichtigste direkt verfuegbare Signal; bei Lerncontent kommt Save/Reach als
   Nutzwert dazu. Likes/Follows bleiben drin, aber ebenfalls normalisiert. */
export function hookPunkte(m, dauerSekunden = null) {
  if (!m) return null;
  const reach = Number(m.reach) || 0;
  if (reach <= 0) return punkte(m);
  const pro = (x) => (Number(x) || 0) / reach;
  let score = pro(m.shares) * 8 + pro(m.saved) * 5 + pro(m.likes) * 2
    + pro(m.comments) * 2 + pro(m.follows) * 12 + pro(m.profile_visits) * 3;
  /* Meta liefert die durchschnittliche Reel-Watch-Time in Millisekunden.
     Normalisiert auf die echte Reel-Dauer misst sie Retention statt bloss
     "laengeres Video = mehr Sekunden". Gedeckelt, damit ein einzelnes
     Watch-Signal Shares/Saves nicht komplett ueberstimmt. */
  const avgMs = Number(m.ig_reels_avg_watch_time) || 0;
  const dauerMs = Number(dauerSekunden) > 0 ? Number(dauerSekunden) * 1000 : 0;
  if (avgMs > 0 && dauerMs > 0) score += Math.min(1.5, avgMs / dauerMs) * 0.5;
  return score;
}

/* Hashtag-Lernschleife: Welche Hashtags stehen unter den Beiträgen, die Follower
   und Reichweite bringen? Gewicht relativ zum Schnitt (0,5–2), plus Summe
   neuer Follower je Hashtag für den Bericht. */
export function hashtagGewichte(eintraege) {
  const mitTags = eintraege.filter((e) => Array.isArray(e.hashtags) && e.hashtags.length);
  if (mitTags.length < 4) return { gewicht: {}, folgen: {} };
  const mittel = mitTags.reduce((a, e) => a + punkte(e.insights), 0) / mitTags.length || 1;
  const g = {}, f = {};
  for (const e of mitTags) for (const h of new Set(e.hashtags.map((x) => x.toLowerCase()))) { (g[h] ||= []).push(punkte(e.insights)); f[h] = (f[h] || 0) + (e.insights.follows || 0); }
  const gewicht = {};
  for (const [h, v] of Object.entries(g)) if (v.length >= 2) gewicht[h] = Math.max(0.5, Math.min(2, (v.reduce((a, b) => a + b, 0) / v.length) / mittel));
  return { gewicht, folgen: f };
}

/* Aus dem Ledger (Einträge mit insights) die Gewichte ableiten. */
/* Ziellänge der Reels ---------------------------------------------------- */

/** Das Fenster, in das eine gemessene Dauer fällt („45-60“), oder null. */
export function dauerFenster(sekunden) {
  if (!(sekunden > 0)) return null;
  const f = CONFIG.reel.dauerFenster.find(([a, b]) => sekunden >= a && sekunden < b);
  /* Alles über dem letzten Fenster zählt zum letzten - sonst fiele ein Reel,
     das ein paar Sekunden überzieht, aus der Messung heraus. */
  const letzte = CONFIG.reel.dauerFenster.at(-1);
  const [a, b] = f || (sekunden >= letzte[0] ? letzte : CONFIG.reel.dauerFenster[0]);
  return `${a}-${b}`;
}

/**
 * Welches Längenfenster als Nächstes drankommt.
 *
 * Solange ein Fenster weniger als dauerMessungen veröffentlichte Reels hat,
 * ist es unerforscht und wird bevorzugt – erst danach entscheidet, was
 * gemessen besser lief. Bei Gleichstand rotiert das Datum, damit der Kanal
 * nicht auf einer Länge festfährt.
 *
 * `min` schneidet die kurzen Fenster ab: Ein komplettes Prüfschema braucht
 * seine Zeit, da wählt der Planer eine Untergrenze und lässt die Lernschleife
 * nur noch darüber entscheiden.
 */
export function dauerWaehlen(datum, strategie = null, { min = 0 } = {}) {
  const erlaubt = CONFIG.reel.dauerFenster.filter(([, b]) => b > min);
  const fenster = (erlaubt.length ? erlaubt : CONFIG.reel.dauerFenster).map(([a, b]) => `${a}-${b}`);
  const messungen = strategie?.dauerMessungen || {};
  const gewicht = strategie?.dauerGewicht || {};
  const tag = Math.floor(Date.parse(`${datum}T12:00:00Z`) / 86400000);
  const offen = fenster.filter((f) => (messungen[f] || 0) < CONFIG.reel.dauerMessungen);
  const auswahl = offen.length ? offen : fenster.filter((f) => (gewicht[f] ?? 1) >= Math.max(...fenster.map((x) => gewicht[x] ?? 1)) - 0.15);
  const liste = auswahl.length ? auswahl : fenster;
  const gewaehlt = liste[((tag % liste.length) + liste.length) % liste.length];
  return CONFIG.reel.dauerFenster.find(([a, b]) => `${a}-${b}` === gewaehlt) || CONFIG.reel.dauerFenster[0];
}

export function strategieAbleiten(ledger, konto = {}) {
  const eintraege = (ledger.veroeffentlicht || []).filter((e) => e.art === "beitrag" && e.insights && punkte(e.insights) != null);
  const strategie = { stand: new Date().toISOString().slice(0, 10), beitraege: eintraege.length, formatGewicht: {}, fachGewicht: {}, hookGewicht: {}, besteStunden: null, follower: konto.follower ?? null, reichweite7: konto.reichweite7 ?? null };
  if (eintraege.length >= 6) {
    const mittel = eintraege.reduce((a, e) => a + punkte(e.insights), 0) / eintraege.length || 1;
    const gruppe = (key, scorer = (m) => punkte(m)) => {
      const g = {};
      for (const e of eintraege) { const k = e[key]; if (!k) continue; (g[k] ||= []).push(scorer(e.insights, e)); }
      const alle = eintraege.map((e) => scorer(e.insights, e)).filter((x) => Number.isFinite(x));
      const basis = alle.reduce((a, b) => a + b, 0) / (alle.length || 1) || 1;
      const out = {};
      for (const [k, v] of Object.entries(g)) if (v.length >= 2) out[k] = Math.max(0.5, Math.min(2, (v.reduce((a, b) => a + b, 0) / v.length) / basis));
      return out;
    };
    strategie.formatGewicht = gruppe("format");
    strategie.fachGewicht = gruppe("fach");
    /* Hooks lernen aus Reaktionen PRO REACH, nicht aus absoluter Reichweite:
       Sonst gewinnt das Muster, das schon ausgespielt wurde, statt das Muster,
       das Menschen zum Weiterleiten/Speichern gebracht hat. */
    strategie.hookGewicht = { ...gruppe("hookTyp", (m, e) => hookPunkte(m, e.dauer)), ...gruppe("hookMuster", (m, e) => hookPunkte(m, e.dauer)) };
  }
  /* Reel-Länge: Wie viele Reels je Fenster gemessen sind und wie sie liefen.
     Die Messungen stehen auch dann schon zur Verfügung, wenn es für Gewichte
     noch zu wenige Beiträge sind - dauerWaehlen braucht sie, um überhaupt
     erst alle Fenster einmal auszuprobieren. */
  const reels = eintraege.filter((e) => e.format === "reel" && e.dauer > 0);
  strategie.dauerMessungen = {};
  for (const e of reels) { const f = dauerFenster(e.dauer); if (f) strategie.dauerMessungen[f] = (strategie.dauerMessungen[f] || 0) + 1; }
  if (reels.length >= 4) {
    const mittelReel = reels.reduce((a, e) => a + punkte(e.insights), 0) / reels.length || 1;
    const g = {};
    for (const e of reels) { const f = dauerFenster(e.dauer); if (f) (g[f] ||= []).push(punkte(e.insights)); }
    strategie.dauerGewicht = {};
    for (const [f, v] of Object.entries(g)) if (v.length >= 2) strategie.dauerGewicht[f] = Math.max(0.5, Math.min(2, (v.reduce((a, b) => a + b, 0) / v.length) / mittelReel));
  } else strategie.dauerGewicht = {};

  const ht = hashtagGewichte(eintraege);
  strategie.hashtagGewicht = ht.gewicht;
  strategie.hashtagFolgen = ht.folgen;
  strategie.folgenGesamt = eintraege.reduce((a, e) => a + (e.insights.follows || 0), 0);
  strategie.profil = konto.profil || null;
  if (konto.onlineStunden) {
    /* UTC-Stunden → lokale Stunden (Europe/Berlin), drei beste mit Mindestabstand 3 h. */
    const offset = (new Date().getTimezoneOffset() === 0 ? 0 : 0) + (istSommerzeit() ? 2 : 1);
    const lokal = Object.entries(konto.onlineStunden).map(([h, n]) => [((Number(h) + offset) % 24), n]).filter(([h]) => h >= 6 && h <= 22).sort((a, b) => b[1] - a[1]);
    const gewaehlt = [];
    for (const [h] of lokal) { if (gewaehlt.every((g) => Math.abs(g - h) >= 3)) gewaehlt.push(h); if (gewaehlt.length === 3) break; }
    if (gewaehlt.length === 3) strategie.besteStunden = gewaehlt.sort((a, b) => a - b).map((h) => hhmm(h * 60 + 30));
  }
  return strategie;
}

function istSommerzeit(d = new Date()) {
  const jan = new Date(d.getFullYear(), 0, 1), jul = new Date(d.getFullYear(), 6, 1);
  const f = new Intl.DateTimeFormat("de-DE", { timeZone: "Europe/Berlin", timeZoneName: "short" });
  return f.format(d).includes("MESZ") || f.formatToParts(d).some((p) => p.type === "timeZoneName" && /MESZ|GMT\+2/.test(p.value));
}

/* Hook-Typ eines Titels (für die Lernschleife). */
export function hookTyp(titel = "") {
  const text = String(titel || "").trim();
  /* Paragraphen-/Artikelnummern sind fachlicher Anker, kein Zahlen-Hook.
     Sonst wuerden neue Titel wie „§ 80 Abs. 5 VwGO?“ faelschlich gegen echte
     Zahlen-Hooks wie „7 Themen …“ gelernt. */
  const ohneNormen = text
    .replace(/§{1,2}\s*\d+[a-z]?(?:\s*Abs\.\s*\d+[a-z]?)?(?:\s*S\.\s*\d+)?/gi, "")
    .replace(/Art\.\s*\d+[a-z]?(?:\s*Abs\.\s*\d+)?/gi, "");
  if (/Fehler|Falle|falsch|übersehen|vergessen|kostet/i.test(text)) return "fehler";
  if (/\?$/.test(text)) return "frage";
  if (/\d/.test(ohneNormen) && /%|€|Tage|Jahre|Prozent|\d{2,}/.test(ohneNormen)) return "zahl";
  return "aussage";
}

/**
 * Wöchentliche Aktualisierung: Insights für Beiträge der letzten 30 Tage
 * nachladen, Strategie neu berechnen. Rückgabe: Strategie + Kontozahlen.
 */
export async function lernschleife(ig, ledger, hosting, { log = console.log } = {}) {
  const grenze = new Date(Date.now() - 30 * 86400000).toISOString().slice(0, 10);
  const offen = (ledger.veroeffentlicht || []).filter((e) => e.art === "beitrag" && e.medienId && e.medienId !== "trocken" && e.datum >= grenze);
  let n = 0;
  let medienTypen = new Map();
  try {
    const liste = await ig.anfrage("GET", `${ig.kontoId}/media`, { fields: "id,media_type,media_product_type,timestamp", limit: 60 });
    for (const m of liste.data || []) medienTypen.set(m.id, m);
  } catch { /* egal */ }
  for (const e of offen) {
    /* Frühestens 48 h nach Veröffentlichung messen, dann alle 7 Tage aktualisieren. */
    const alter = (Date.now() - new Date(e.veroeffentlicht || `${e.datum}T12:00:00Z`).getTime()) / 86400000;
    if (alter < 2) continue;
    if (e.insightsStand && (Date.now() - new Date(e.insightsStand).getTime()) / 86400000 < 7 && alter > 9) continue;
    const m = await medienInsights(ig, medienTypen.get(e.medienId) || { id: e.medienId, media_type: e.format === "reel" ? "VIDEO" : "CAROUSEL_ALBUM" });
    if (m) { e.insights = m; e.insightsStand = new Date().toISOString(); n++; }
  }
  const konto = await kontoInsights(ig);
  const strategie = strategieAbleiten(ledger, konto);
  hosting.jsonSchreiben("strategie.json", strategie);
  /* Follower-Verlauf für den Bericht. */
  const verlauf = hosting.jsonLesen("follower.json", []);
  if (konto.follower != null) { verlauf.push({ datum: new Date().toISOString().slice(0, 10), follower: konto.follower, reichweite7: konto.reichweite7 }); hosting.jsonSchreiben("follower.json", verlauf.slice(-400)); }
  log(`Lernschleife: ${n} Beiträge gemessen · ${strategie.beitraege} bewertet · Follower ${konto.follower ?? "?"} · beste Zeiten ${strategie.besteStunden?.join(", ") || "Standard"}`);
  return { strategie, konto };
}
