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
/* Wachstumskennzahlen: neue Follower und Profilbesuche je Beitrag – nicht jede
   API-Version liefert sie, deshalb mit Rückfall auf die Grundmetriken. */
const METRIKEN_WACHSTUM = "follows,profile_visits";

function werte(r) {
  const o = {};
  for (const m of r.data || []) o[m.name] = m.values?.[0]?.value ?? m.total_value?.value ?? 0;
  return o;
}

/* Kennzahlen eines Mediums (Fehler → null, z. B. fehlende Berechtigung). */
export async function medienInsights(ig, medium) {
  const basis = medium.media_type === "VIDEO" || medium.media_product_type === "REELS" ? METRIKEN_REEL : METRIKEN_BILD;
  try {
    try {
      return werte(await ig.anfrage("GET", `${medium.id}/insights`, { metric: `${basis},${METRIKEN_WACHSTUM}` }, { versuche: 1 }));
    } catch {
      return werte(await ig.anfrage("GET", `${medium.id}/insights`, { metric: basis }));
    }
  } catch {
    return null;
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
export function strategieAbleiten(ledger, konto = {}) {
  const eintraege = (ledger.veroeffentlicht || []).filter((e) => e.art === "beitrag" && e.insights && punkte(e.insights) != null);
  const strategie = { stand: new Date().toISOString().slice(0, 10), beitraege: eintraege.length, formatGewicht: {}, fachGewicht: {}, hookGewicht: {}, besteStunden: null, follower: konto.follower ?? null, reichweite7: konto.reichweite7 ?? null };
  if (eintraege.length >= 6) {
    const mittel = eintraege.reduce((a, e) => a + punkte(e.insights), 0) / eintraege.length || 1;
    const gruppe = (key) => {
      const g = {};
      for (const e of eintraege) { const k = e[key]; if (!k) continue; (g[k] ||= []).push(punkte(e.insights)); }
      const out = {};
      for (const [k, v] of Object.entries(g)) if (v.length >= 2) out[k] = Math.max(0.5, Math.min(2, (v.reduce((a, b) => a + b, 0) / v.length) / mittel));
      return out;
    };
    strategie.formatGewicht = gruppe("format");
    strategie.fachGewicht = gruppe("fach");
    /* Hooks: Gemessen wird das erkannte Muster; bei Reels steht zusätzlich das
       beauftragte Muster im Ledger. Beides fließt in dieselbe Tabelle, damit die
       Rotation in hooks.mjs davon lernt. */
    strategie.hookGewicht = { ...gruppe("hookTyp"), ...gruppe("hookMuster") };
  }
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
  if (/\d/.test(titel) && /%|€|Tage|Jahre|Prozent|\d{2,}/.test(titel)) return "zahl";
  if (/Fehler|Falle|falsch|übersehen|vergessen|kostet/i.test(titel)) return "fehler";
  if (/\?$/.test(titel.trim())) return "frage";
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
