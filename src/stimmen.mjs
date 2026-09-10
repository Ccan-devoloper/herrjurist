/* ==========================================================================
   Welche Stimme spricht die Reels?

   Zwei Schritte, beide ohne Zutun:

   1. Auswahl. Aus der ElevenLabs-Stimmenbibliothek werden deutsche Stimmen
      gesucht, die zu einem Lernkanal passen: Muttersprachler, erwachsen,
      ruhig erzählend oder erklärend. Aus der Trefferliste bleiben drei
      Kandidaten übrig (state/stimmen.json). Nach welchen Merkmalen sortiert
      wird, steht in BEWERTUNG – Klang lässt sich nicht rechnen, Eignung
      schon.

   2. Lernen. Welche der drei tatsächlich ankommt, entscheidet das Publikum.
      Jedes Reel bekommt eine Stimme zugeteilt, im Ledger steht sie beim
      Beitrag, und die Zahlen (insights.mjs) sagen später, welche die
      Reichweite trägt. Gewählt wird wie bei den Uhrzeiten nach UCB1:
      optimistisch bei Unsicherheit. Steht eine Stimme deutlich vorn, hört
      die Rotation auf – ein Kanal, der jede Woche anders klingt, wird nicht
      wiedererkannt.
   ========================================================================== */

import { CONFIG } from "./config.mjs";
import { punkte } from "./insights.mjs";

const API = "https://api.elevenlabs.io/v1";

/* Merkmale, die für einen Lernkanal sprechen. Der Wert ist ein Aufschlag auf
   die Grundpunktzahl; negative Werte schließen aus. */
const BEWERTUNG = {
  sprache: { de: 3 },
  /* Erzählend oder erklärend – kein Werbe- oder Hörbuchpathos. */
  einsatz: { narrative_story: 2, informative_educational: 3, news: 1, entertainment_tv: 0.5, social_media: 1.5, advertisement: -2, characters_animation: -3 },
  alter: { middle_aged: 2, young: 1, old: 0 },
  /* Beschreibungen aus der Bibliothek: ruhig und klar schlägt „dramatic“. */
  beschreibung: { calm: 2, confident: 2, professional: 2, casual: 1, friendly: 1, warm: 1, crisp: 1, deep: 0.5, excited: -1, dramatic: -2, whisper: -3, raspy: -1 },
};

const wert = (tabelle, schluessel) => tabelle[String(schluessel || "").toLowerCase()] ?? 0;

/**
 * Bewertet eine Stimme aus der Bibliothek. Rückgabe null heißt: kommt nicht in
 * Frage (falsche Sprache, für das kostenlose Abo gesperrt, Kinderstimme …).
 */
export function stimmeBewerten(v) {
  const sprache = String(v.language || v.fine_tuning?.language || "").toLowerCase();
  if (sprache && sprache !== "de") return null;
  if (/child|young_child/i.test(v.age || "")) return null;
  let p = wert(BEWERTUNG.sprache, sprache) + wert(BEWERTUNG.einsatz, v.use_case) + wert(BEWERTUNG.alter, v.age);
  for (const [begriff, bonus] of Object.entries(BEWERTUNG.beschreibung)) {
    if (new RegExp(begriff, "i").test(`${v.descriptive || ""} ${v.description || ""}`)) p += bonus;
  }
  if (p < 0) return null;
  /* Wie oft andere die Stimme benutzen, ist das einzige echte Publikumsurteil,
     das vor dem ersten eigenen Reel vorliegt – aber nur ein leichter Daumen. */
  const nutzung = Number(v.cloned_by_count || 0) + Number(v.usage_character_count_1y || 0) / 1e6;
  return { id: v.voice_id, name: v.name, geschlecht: v.gender || null, alter: v.age || null, einsatz: v.use_case || null,
    beschreibung: v.descriptive || null, akzent: v.accent || null, besitzer: v.public_owner_id || null,
    punkte: Number((p + Math.log10(1 + nutzung) * 0.6).toFixed(2)) };
}

async function api(pfad, opt = {}) {
  const res = await fetch(`${API}${pfad}`, { ...opt, headers: { "xi-api-key": CONFIG.reel.elevenlabsKey, ...(opt.body ? { "Content-Type": "application/json" } : {}), ...(opt.headers || {}) } });
  if (!res.ok) throw new Error(`ElevenLabs ${res.status} ${pfad}: ${(await res.text()).slice(0, 200)}`);
  return res.json();
}

/** Tarif des Kontos: „free“, „starter“, „creator“ … */
export async function tarif() {
  try { return String((await api("/user/subscription")).tier || "").toLowerCase(); } catch { return ""; }
}

/* Stimmen des eigenen Kontos. Achtung: Eine aus der Bibliothek übernommene
   Stimme steht hier ebenfalls (category „professional“), darf im kostenlosen
   Tarif aber weiterhin nicht sprechen – sie käme sonst durch die Hintertür
   zurück in die Auswahl. Frei nutzbar sind nur die vorinstallierten
   („premade“); sie lesen Deutsch mit den mehrsprachigen Modellen, je nach
   Stimme mit leichtem englischem Einschlag. */
async function kontoStimmen({ nurFrei = false } = {}) {
  const j = await api("/voices");
  const out = [];
  for (const v of j.voices || []) {
    if (nurFrei && String(v.category || "").toLowerCase() !== "premade") continue;
    const b = stimmeBewerten({ ...v, language: "de", use_case: v.labels?.use_case, age: v.labels?.age,
      descriptive: v.labels?.descriptive || v.labels?.description, gender: v.labels?.gender, accent: v.labels?.accent });
    if (b) out.push({ ...b, quelle: "konto", kategorie: v.category || null });
  }
  return out;
}

/**
 * Sucht deutsche Stimmen.
 *
 * Wichtig fürs kostenlose Abo: Bibliotheksstimmen darf es über die API NICHT
 * sprechen lassen („Free users cannot use library voices via the API“, HTTP
 * 402). Deshalb werden dort nur die Stimmen des eigenen Kontos betrachtet –
 * die vorinstallierten mehrsprachigen. Erst ein bezahlter Tarif öffnet die
 * Bibliothek mit deutschen Muttersprachlern.
 * @returns {Promise<Array>} bewertete Kandidaten, beste zuerst
 */
export async function kandidatenSuchen({ anzahl = 3, abo = null } = {}) {
  const gefunden = [];
  const bezahlt = (abo ?? (await tarif())) !== "free";
  if (bezahlt) {
    try {
      /* Zwei Anfragen, damit beide Geschlechter vertreten sind – die Bibliothek
         sortiert sonst leicht einseitig. */
      for (const geschlecht of ["male", "female"]) {
        const j = await api(`/shared-voices?page_size=60&language=de&gender=${geschlecht}&sort=trending`);
        for (const v of j.voices || []) { const b = stimmeBewerten(v); if (b) gefunden.push({ ...b, quelle: "bibliothek" }); }
      }
    } catch (e) {
      console.warn(`  ! Stimmenbibliothek nicht erreichbar: ${e.message}`);
    }
  }
  if (!gefunden.length) gefunden.push(...(await kontoStimmen({ nurFrei: !bezahlt })));
  const sortiert = gefunden.sort((a, b) => b.punkte - a.punkte);
  /* Nicht drei Varianten derselben Stimmlage: je Geschlecht höchstens zwei. */
  const auswahl = [], jeGeschlecht = {};
  for (const v of sortiert) {
    const g = v.geschlecht || "?";
    if ((jeGeschlecht[g] || 0) >= 2) continue;
    jeGeschlecht[g] = (jeGeschlecht[g] || 0) + 1;
    auswahl.push(v);
    if (auswahl.length === anzahl) break;
  }
  return auswahl;
}

/**
 * Macht eine Bibliotheksstimme im eigenen Konto benutzbar (Voice-ID des
 * Kontos). Kontostimmen gehen unverändert durch.
 */
export async function stimmeUebernehmen(v, { bezahlt = true } = {}) {
  /* Im kostenlosen Tarif bringt das Übernehmen nichts: Die Stimme landet zwar
     im Konto, sprechen darf sie trotzdem nicht – und verstopft nur den Platz. */
  if (v.quelle !== "bibliothek" || !v.besitzer || !bezahlt) return v;
  try {
    const j = await api(`/voices/add/${encodeURIComponent(v.besitzer)}/${encodeURIComponent(v.id)}`, { method: "POST", body: JSON.stringify({ new_name: v.name }) });
    return { ...v, id: j.voice_id || v.id, uebernommen: true };
  } catch (e) {
    /* Das kostenlose Abo erlaubt nur wenige eigene Stimmen. Dann bleibt die
       Bibliotheks-ID – für viele Stimmen genügt sie zum Sprechen. */
    console.warn(`  ! Stimme ${v.name} nicht übernommen: ${e.message}`);
    return v;
  }
}

/* --- Lernen: welche Stimme trägt die Reichweite? ------------------------- */

/** Zahlen je Stimme aus dem Ledger: Anzahl gemessener Reels und ihr Mittel. */
export function stimmenStatistik(ledger, heute = new Date()) {
  const reife = new Date(heute.getTime() - CONFIG.plan.zeitReifeTage * 86400000).toISOString().slice(0, 10);
  const reels = (ledger?.veroeffentlicht || []).filter((e) => e.art === "beitrag" && e.format === "reel" && e.stimmeId && e.insights && punkte(e.insights) != null && (e.datum || "9999") <= reife);
  const mittel = reels.length ? reels.reduce((a, e) => a + punkte(e.insights), 0) / reels.length : 0;
  const je = {};
  for (const e of reels) (je[e.stimmeId] ||= { n: 0, summe: 0, name: e.stimmeName || e.stimmeId }).n++, (je[e.stimmeId].summe += punkte(e.insights));
  const tabelle = Object.fromEntries(Object.entries(je).map(([id, v]) => [id, { n: v.n, name: v.name, mittel: mittel > 0 ? v.summe / v.n / mittel : 1 }]));
  const mitWirkung = reels.filter((e) => punkte(e.insights) > 0).length;
  return { gesamt: reels.length, mitWirkung, mittelPunkte: mittel, je: tabelle };
}

/**
 * Steht eine Stimme fest? Nur wenn jede Kandidatin oft genug gemessen wurde
 * und die beste die zweitbeste deutlich schlägt – sonst wäre es Rauschen.
 */
export function gewinner(statistik, kandidaten, { mindestens = CONFIG.reel.stimmeMessungen, vorsprung = CONFIG.reel.stimmeVorsprung } = {}) {
  const zeilen = kandidaten.map((k) => ({ ...k, ...(statistik.je[k.id] || { n: 0, mittel: 1 }) })).sort((a, b) => b.mittel - a.mittel);
  if (zeilen.length < 2 || zeilen.some((z) => z.n < mindestens)) return null;
  if (statistik.mittelPunkte < CONFIG.plan.zeitMindestWirkung) return null;
  return zeilen[0].mittel >= zeilen[1].mittel + vorsprung ? zeilen[0] : null;
}

/**
 * Stimme für das nächste Reel. Steht der Gewinner fest, spricht immer er;
 * sonst wird nach UCB1 verteilt: wer selten dran war, kommt eher dran.
 * @returns {{id:string,name:string}|null} null = keine Auswahl hinterlegt
 */
export function stimmeWaehlen({ kandidaten, ledger, datum, fest = null, zufall = Math.random }) {
  if (CONFIG.reel.stimme && !CONFIG.reel.stimmeLernen) return { id: CONFIG.reel.stimme, name: "fest eingestellt" };
  if (!kandidaten?.length) return CONFIG.reel.stimme ? { id: CONFIG.reel.stimme, name: "fest eingestellt" } : null;
  if (fest) return fest;
  const stat = stimmenStatistik(ledger, datum ? new Date(`${datum}T12:00:00Z`) : new Date());
  const gesamt = Math.max(1, stat.gesamt);
  const bewertet = kandidaten.map((k) => {
    const s = stat.je[k.id] || { n: 0, mittel: 1 };
    return { ...k, n: s.n, wert: s.mittel + CONFIG.reel.stimmeErkundung * Math.sqrt(Math.log(gesamt + 1) / (s.n + 1)) };
  });
  const beste = Math.max(...bewertet.map((b) => b.wert));
  const spitze = bewertet.filter((b) => b.wert >= beste - 1e-9);
  const w = spitze[Math.floor(zufall() * spitze.length)];
  return { id: w.id, name: w.name };
}

/** Zeile für den Wochenbericht. */
export function stimmenBericht(ledger, kandidaten = []) {
  const stat = stimmenStatistik(ledger);
  if (!stat.gesamt) return null;
  const zeilen = kandidaten.map((k) => ({ name: k.name, ...(stat.je[k.id] || { n: 0, mittel: 1 }) })).sort((a, b) => b.mittel - a.mittel);
  const sieger = gewinner(stat, kandidaten);
  return { gesamt: stat.gesamt, zeilen, sieger: sieger ? sieger.name : null };
}
