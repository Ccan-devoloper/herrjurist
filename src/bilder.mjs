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
import { CONFIG } from "./config.mjs";

const API = "https://api.pexels.com/v1/search";

/* Hochformat passt auf keine Kachel gut: Wir brauchen Bilder, die sich in ein
   breites Feld schneiden lassen, ohne dass Köpfe abgeschnitten werden. */
const MINDESTBREITE = 1200;

/** Bewertet einen Treffer: quer, groß genug, nicht zu dunkel-monoton. */
function taugt(foto) {
  if (!foto?.src?.large2x) return false;
  if (foto.width < MINDESTBREITE) return false;
  return foto.width >= foto.height;      // quer oder quadratisch
}

/**
 * Sucht ein Foto zu einer Szene.
 * @param {string} szene englische Beschreibung, z. B. "delivery man waiting at front door"
 * @returns {Promise<{url:string,fotograf:string,seite:string}|null>}
 */
export async function fotoSuchen(szene, { zufall = Math.random } = {}) {
  const key = CONFIG.bilder.key;
  if (!key || !szene) return null;
  const url = `${API}?query=${encodeURIComponent(szene)}&per_page=15&orientation=landscape&locale=en-US`;
  try {
    const res = await fetch(url, { headers: { Authorization: key } });
    if (!res.ok) { console.warn(`  ! Pexels ${res.status}: ${(await res.text()).slice(0, 120)}`); return null; }
    const j = await res.json();
    const treffer = (j.photos || []).filter(taugt);
    if (!treffer.length) return null;
    /* Nicht immer das erste Bild: Sonst tragen zwei Beiträge zum selben
       Themenkreis dasselbe Foto. Aus den besten fünf wird gewürfelt. */
    const auswahl = treffer.slice(0, 5);
    const f = auswahl[Math.floor(zufall() * auswahl.length)];
    return { url: f.src.large2x, fotograf: f.photographer || "", seite: f.url || "", id: f.id };
  } catch (e) {
    console.warn(`  ! Pexels nicht erreichbar: ${e.message}`);
    return null;
  }
}

/**
 * Lädt ein Foto und gibt es als data:-URI zurück. Der Renderer baut die Seite
 * in einer temporären Datei zusammen; ein Dateipfad darin wäre je nach
 * Arbeitsverzeichnis mal gültig und mal nicht, eine data:-URI immer.
 * @param {string} [ablage] optionales Verzeichnis, in dem das Original zur
 *   Nachschau liegen bleibt
 */
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
 * Foto für die Titelfolie eines Beitrags besorgen. Gibt { bild, quelle } oder
 * null zurück – null heißt: Icon-Bühne wie bisher.
 */
export async function titelbild(beitrag, ablage = null, opt = {}) {
  if (!CONFIG.bilder.aktiv || !CONFIG.bilder.key) return null;
  const szene = beitrag?.bildSzene || beitrag?.folien?.[0]?.bildSzene;
  if (!szene) return null;
  const foto = await fotoSuchen(szene, opt);
  if (!foto) { console.log(`  → kein Foto zu „${szene}“ – Titelfolie bleibt beim Icon.`); return null; }
  const bild = await fotoLaden(foto, ablage);
  if (!bild) return null;
  console.log(`  → Titelbild: „${szene}“ · ${foto.fotograf || "Pexels"}`);
  return { bild, quelle: `Foto: ${foto.fotograf || "Pexels"} / Pexels`, seite: foto.seite };
}
