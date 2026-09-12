/* ==========================================================================
   Bilder für die Titelfolie (Pexels).

   Der Gedanke: Ein Stichwort wie „Annahmeverzug“ findet bei Pexels nichts –
   und was es findet, ist der immer gleiche Richterhammer. Deshalb liefert der
   Autor keine juristische Vokabel, sondern eine SZENE („Mann wartet mit
   Pizzakartons vor einer Haustür“). Danach wird gesucht, auf Englisch, weil
   die Bibliothek englisch verschlagwortet ist.

   Findet sich nichts Passendes, gibt es kein Bild – dann bleibt es beim Icon.
   Ein beliebiges Symbolfoto ist schlechter als gar keines: Es sagt nichts und
   sieht aus wie jeder andere Jura-Account.

   Pexels verlangt für die API-Nutzung einen sichtbaren Hinweis auf die Quelle;
   der steht klein auf der Kachel (vorlagen.mjs, .bildquelle).
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { CONFIG } from "./config.mjs";
import { freistellen } from "./freistellen.mjs";

const API = "https://api.pexels.com/v1/search";

/* Hochformat passt auf keine Kachel gut: Wir brauchen Bilder, die sich in ein
   breites Feld schneiden lassen, ohne dass Köpfe abgeschnitten werden. */
const MINDESTBREITE = 1200;

/* Bildbeschreibungen, die auf der Kachel nichts verloren haben: Masken- und
   Pandemiefotos (Pexels ist voll davon, seit 2020), Stockfoto-Klischees. */
const UNERWUENSCHT = /\b(mask|masks|covid|corona|pandemic|quarantine|vaccine|virus|ppe|handshake|thumbs up|stock photo)\b/i;
/* Wörter der Szene, die in der Bildbeschreibung wiederkehren sollten. */
const FUELLWOERTER = new Set(["a", "an", "the", "of", "in", "on", "at", "with", "and", "to", "for", "from", "by", "his", "her", "their", "its", "while", "near", "into", "over", "under", "person", "people", "man", "woman", "young", "old"]);
function schluesselwoerter(szene) {
  return String(szene).toLowerCase().replace(/[^a-z\s-]/g, " ").split(/\s+/).filter((w) => w.length > 2 && !FUELLWOERTER.has(w));
}

/** Bewertet einen Treffer: quer, groß genug, ohne unerwünschte Beschreibung. */
function taugt(foto) {
  if (!foto?.src?.large2x) return false;
  if (foto.width < MINDESTBREITE) return false;
  if (UNERWUENSCHT.test(foto.alt || "")) return false;
  return foto.width >= foto.height;      // quer oder quadratisch
}

/* Passung zur Szene: Wie viele Wörter der Szene nennt die Bildbeschreibung
   (Wortstämme, damit „letter“ auch „letters“ trifft)? Pexels sortiert nach
   Beliebtheit, nicht nach Passung - das erste Ergebnis zu „woman reading
   letter“ kann ein Porträt ohne Brief sein. */
export function passung(foto, szene) {
  const alt = String(foto?.alt || "").toLowerCase();
  const woerter = schluesselwoerter(szene);
  if (!woerter.length) return 0;
  const treffer = woerter.filter((w) => alt.includes(w.length > 5 ? w.slice(0, -1) : w)).length;
  return treffer / woerter.length;
}

/**
 * Sucht ein Foto zu einer Szene.
 * @param {string} szene englische Beschreibung, z. B. "delivery man waiting at front door"
 * @returns {Promise<{url:string,fotograf:string,seite:string}|null>}
 */
/**
 * Kandidaten zu einer Szene, beste Passung zuerst. Mehrere, weil erst der
 * Freisteller zeigt, ob ein Foto taugt - das erste kann unscharf sein oder
 * ein am Rand angeschnittenes Motiv haben.
 */
export async function fotoKandidaten(szene, { zufall = Math.random, anzahl = 4 } = {}) {
  const key = CONFIG.bilder.key;
  if (!key || !szene) return [];
  const url = `${API}?query=${encodeURIComponent(szene)}&per_page=20&orientation=landscape&locale=en-US`;
  try {
    const res = await fetch(url, { headers: { Authorization: key } });
    if (!res.ok) { console.warn(`  ! Pexels ${res.status}: ${(await res.text()).slice(0, 120)}`); return []; }
    const j = await res.json();
    const treffer = (j.photos || []).filter(taugt).map((f) => ({ url: f.src.large2x, fotograf: f.photographer || "", seite: f.url || "", id: f.id, alt: f.alt || "", passung: passung(f, szene) }));
    if (!treffer.length) return [];
    /* Beste Passung zuerst; unter gleich guten wird gewürfelt, damit zwei
       Beiträge zum selben Themenkreis nicht dasselbe Foto tragen. */
    treffer.sort((a, b) => b.passung - a.passung || zufall() - 0.5);
    /* Beschreibungen ganz ohne Bezug zur Szene fliegen raus, sobald es
       bessere gibt. */
    const mitBezug = treffer.filter((t) => t.passung > 0);
    return (mitBezug.length ? mitBezug : treffer).slice(0, anzahl);
  } catch (e) {
    console.warn(`  ! Pexels nicht erreichbar: ${e.message}`);
    return [];
  }
}

/** Erster Kandidat zu einer Szene (für Aufrufer, die nur ein Foto brauchen). */
export async function fotoSuchen(szene, opt = {}) {
  const [erster] = await fotoKandidaten(szene, { ...opt, anzahl: 1 });
  return erster || null;
}

/**
 * Lädt ein Foto und gibt es als data:-URI zurück. Der Renderer baut die Seite
 * in einer temporären Datei zusammen; ein Dateipfad darin wäre je nach
 * Arbeitsverzeichnis mal gültig und mal nicht, eine data:-URI immer.
 * @param {string} [ablage] optionales Verzeichnis, in dem das Original zur
 *   Nachschau liegen bleibt
 */
export async function fotoDatei(foto, ablage) {
  if (!foto?.url) return null;
  try {
    const res = await fetch(foto.url);
    if (!res.ok) return null;
    fs.mkdirSync(ablage, { recursive: true });
    const datei = path.join(ablage, `pexels-${foto.id || Date.now()}.jpg`);
    fs.writeFileSync(datei, Buffer.from(await res.arrayBuffer()));
    return datei;
  } catch (e) {
    console.warn(`  ! Foto nicht ladbar: ${e.message}`);
    return null;
  }
}

export async function fotoLaden(foto, ablage = null) {
  if (!foto?.url) return null;
  try {
    const res = await fetch(foto.url);
    if (!res.ok) return null;
    const puffer = Buffer.from(await res.arrayBuffer());
    if (ablage) {
      fs.mkdirSync(ablage, { recursive: true });
      fs.writeFileSync(path.join(ablage, `pexels-${foto.id || Date.now()}.jpg`), puffer);
    }
    return `data:image/jpeg;base64,${puffer.toString("base64")}`;
  } catch (e) {
    console.warn(`  ! Foto nicht ladbar: ${e.message}`);
    return null;
  }
}

/**
 * Foto für die Titelfolie eines Beitrags besorgen – freigestellt, damit das
 * Motiv aus der Kachel läuft statt als Rechteck darauf zu liegen.
 * Gibt { bild, quelle, frei } oder null zurück; null heißt: Icon-Bühne.
 */
export async function titelbild(beitrag, ablage = null, opt = {}) {
  if (!CONFIG.bilder.aktiv || !CONFIG.bilder.key) return null;
  /* Zwei Szenen vom Autor: Liefert die erste nichts Brauchbares, die zweite. */
  const szenen = [beitrag?.bildSzene || beitrag?.folien?.[0]?.bildSzene, beitrag?.bildSzeneAlt || beitrag?.folien?.[0]?.bildSzeneAlt].filter(Boolean);
  if (!szenen.length) return null;
  let ersterRoh = null, erstesFoto = null, ersteSzene = null;
  for (const szene of szenen) {
    const kandidaten = await fotoKandidaten(szene, opt);
    if (!kandidaten.length) { console.log(`  → kein Foto zu „${szene}“.`); continue; }
    for (const foto of kandidaten) {
      /* Erst als Datei laden: Zum Freistellen braucht rembg einen Pfad. */
      const roh = await fotoDatei(foto, ablage || os.tmpdir());
      if (!roh) continue;
      if (!ersterRoh) { ersterRoh = roh; erstesFoto = foto; ersteSzene = szene; }
      const quelle = `Foto: ${foto.fotograf || "Pexels"} / Pexels`;
      if (!CONFIG.bilder.freistellen) {
        console.log(`  → Titelbild: „${szene}“ · ${foto.fotograf || "Pexels"}`);
        return { bild: `data:image/jpeg;base64,${fs.readFileSync(roh).toString("base64")}`, quelle, seite: foto.seite, frei: false };
      }
      /* Der Freisteller entscheidet: unscharf, angeschnitten oder ohne
         erkennbares Motiv heißt nächster Kandidat. */
      const frei = freistellen(roh, { randFarbe: opt.randFarbe || null });
      if (!frei) continue;
      const bild = `data:image/png;base64,${fs.readFileSync(frei.pfad).toString("base64")}`;
      fs.rmSync(frei.pfad, { force: true });
      console.log(`  → Titelbild freigestellt: „${szene}“ · ${foto.fotograf || "Pexels"} (Deckung ${(frei.deckung * 100).toFixed(0)} %, Passung ${(foto.passung * 100).toFixed(0)} %)`);
      /* Die Maße wandern mit: Die Vorlage rechnet daraus die Bühne aus, damit
         ein breites Motiv nicht als Briefmarke in der Ecke endet. */
      return { bild, quelle, seite: foto.seite, frei: true, breite: frei.breite || null, hoehe: frei.hoehe || null };
    }
  }
  console.log(`  → kein brauchbares Motiv zu „${szenen.join("“ / „")}“ – Titelfolie bleibt beim Icon.`);
  /* Freistellen misslungen: lieber kein Bild als ein aufgeklebtes Rechteck. */
  if (!CONFIG.bilder.rechteckErlaubt || !ersterRoh) return null;
  console.log(`  → Titelbild als Karte: „${ersteSzene}“ · ${erstesFoto.fotograf || "Pexels"}`);
  return { bild: `data:image/jpeg;base64,${fs.readFileSync(ersterRoh).toString("base64")}`, quelle: `Foto: ${erstesFoto.fotograf || "Pexels"} / Pexels`, seite: erstesFoto.seite, frei: false };
}
