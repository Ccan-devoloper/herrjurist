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
import { bildKiAktiv, motivZeichnen, motivHervorholen } from "./bildki.mjs";
import { archivLaden, passendesMotiv, motivAblegen, verwendungVermerken } from "./motivarchiv.mjs";
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
/* Deterministischer Notfall fuer alte/fehlerhafte Entwuerfe ohne bildSzene.
   Das Cover bleibt damit fotografierbar, statt still auf eine reine Icon-Kachel zurueckzufallen. */
export function fallbackBildSzene(beitrag = {}) {
  const icon = beitrag?.folien?.find((f) => f.art === "titel")?.icon || beitrag?.icon || "";
  const szenen = {
    kalender: "calendar beside document folder", uhr: "desk clock beside case file",
    vertrag: "signed contract on wooden desk", dokument: "stapled case file on desk",
    schriftrolle: "sealed paper beside document folder", umschlag: "unopened letter beside case file",
    haus: "house keys beside document folder", schluessel: "house keys beside case file",
    auto: "parked car beside case folder", polizei: "police case folder on desk",
    messer: "kitchen knife beside evidence folder", personen: "students reviewing case files",
    person: "student reviewing case file", lupe: "magnifying glass beside case file",
    globus: "travel documents beside case folder", buch: "open notebook beside case files",
    warnung: "red folder beside deadline calendar",
  };
  return szenen[icon] || "student reviewing case files";
}
/* Kostenloser Primärpfad für Cover: ein echtes Pexels-Foto wird zuerst
   freigestellt; wenn alle Freisteller scheitern, ist eine saubere Fotokarte
   immer noch besser als eine reine Icon-Kachel oder ein bezahlter Bildaufruf.
   Der alte Schalter rechteckErlaubt gilt damit nicht für diesen letzten
   Cover-Notfall – die neue Produktregel „Foto + Icon“ hat Vorrang. */
async function kostenlosesCoverFoto(szenen, ablage, opt = {}) {
  if (!CONFIG.bilder.key) return null;
  let notfall = null;
  for (const szene of szenen) {
    const kandidaten = await fotoKandidaten(szene, opt);
    for (const foto of kandidaten) {
      const roh = await fotoDatei(foto, ablage || os.tmpdir());
      if (!roh) continue;
      const quelle = `Foto: ${foto.fotograf || "Pexels"} / Pexels`;
      if (!notfall) notfall = { roh, foto, szene, quelle };
      if (!CONFIG.bilder.freistellen) {
        return { bild: `data:image/jpeg;base64,${fs.readFileSync(roh).toString("base64")}`, quelle, seite: foto.seite, frei: false, typ: "foto" };
      }
      const frei = freistellen(roh, { randFarbe: opt.randFarbe || null });
      if (!frei) continue;
      const bild = `data:image/png;base64,${fs.readFileSync(frei.pfad).toString("base64")}`;
      fs.rmSync(frei.pfad, { force: true });
      console.log(`  → kostenloses Coverfoto: „${szene}“ · ${foto.fotograf || "Pexels"}`);
      return { bild, quelle, seite: foto.seite, frei: true, breite: frei.breite || null, hoehe: frei.hoehe || null, typ: "foto" };
    }
  }
  if (!notfall) return null;
  console.log(`  → kostenloses Coverfoto als Karte: „${notfall.szene}“ · ${notfall.foto.fotograf || "Pexels"}`);
  return { bild: `data:image/jpeg;base64,${fs.readFileSync(notfall.roh).toString("base64")}`, quelle: notfall.quelle, seite: notfall.foto.seite, frei: false, typ: "foto" };
}
export async function titelbild(beitrag, ablage = null, opt = {}) {
  if (!CONFIG.bilder.aktiv) return null;
  /* Zwei Szenen vom Autor: Liefert die erste nichts Brauchbares, die zweite. */
  const fallback = fallbackBildSzene(beitrag);
  const szenen = [beitrag?.bildSzene || beitrag?.folien?.[0]?.bildSzene || fallback, beitrag?.bildSzeneAlt || beitrag?.folien?.[0]?.bildSzeneAlt].filter(Boolean);
  if (!szenen.includes(fallback)) szenen.push(fallback);

  /* Zeichnen geht vor Suchen: Das Motiv entsteht zum Thema und kommt
     freigestellt - kein Stockfoto, das danebenliegt, kein Freisteller, der
     misslingt, kein Bildnachweis auf der Kachel. Misslingt es, bleibt die
     Titelfolie beim Icon; die Fotosuche springt dann nicht ein, sie war ja
     der Grund für die Umstellung. */
  if (bildKiAktiv()) {
    /* Gezeichnet wird nur, was im Feed steht: Titelfolien und Reel-Cover.
       Neun Stories am Tag mitzuzeichnen wäre das Vierfache an Bildern und
       spränge den Tagesdeckel; Stories bleiben beim Icon, das dort ohnehin
       ruhiger wirkt. */
    if (opt.ki === false) return null;
    const archivDir = opt.archivDir || null;
    const datum = opt.datum || new Date().toISOString().slice(0, 10);
    const archiv = archivDir ? archivLaden(archivDir) : null;
    /* Ein Foto-Cover darf nicht mit einer flachen Figur aus dem Archiv
       bedient werden und umgekehrt - sonst mischen sich die Looks im Feed. */
    /* Cover sind fest fotorealistisch; nur Erklaerfiguren im Reel bleiben flach. */
    const look = (opt.zweck || "bild") === "erklaerbild" ? "flach" : "foto";
    /* Erst im Archiv nachsehen: Ein Motiv, das lange genug her ist und zur
       Szene passt, kostet nichts mehr. */
    if (archiv) {
      for (const szene of szenen) {
        const fund = passendesMotiv(archiv, szene, datum, { mindestTage: CONFIG.bilder.ki.wiederTage, schwelle: CONFIG.bilder.ki.aehnlich, themaId: beitrag?.themaId || null, look });
        if (!fund) continue;
        const wieder = motivHervorholen(path.join(archivDir, fund.eintrag.datei), { randFarbe: opt.randFarbe || null });
        if (!wieder) continue;
        verwendungVermerken(archivDir, archiv, fund.eintrag, datum);
        const bild = `data:image/png;base64,${fs.readFileSync(wieder.pfad).toString("base64")}`;
        fs.rmSync(wieder.pfad, { force: true });
        console.log(`  → Motiv aus dem Archiv: „${fund.eintrag.szene}" für „${szene}" (${fund.alter} Tage alt, ${(fund.aehnlich * 100).toFixed(0)} % Übereinstimmung) - kostet nichts.`);
        return { bild, quelle: null, seite: null, frei: true, breite: wieder.breite, hoehe: wieder.hoehe, typ: look === "foto" ? "foto" : "illustration" };
      }
    }
    /* Kostenlose reale Fotografie vor Bild-KI: Der Tagesdeckel soll für
       Pflichttext und Faktenprüfung frei bleiben. */
    if ((opt.zweck || "bild") !== "erklaerbild" && opt.ki !== false) {
      const gratis = await kostenlosesCoverFoto(szenen, ablage, opt);
      if (gratis) return gratis;
    }
    /* Erklaervideo mit vielen Szenen: Ab dem Deckel wird nicht mehr gezeichnet,
       aber weiter im Archiv gesucht - ein passendes altes Motiv ist immer
       besser als die wiederholte Figur der Nachbarszene und kostet nichts. */
    if (opt.nurArchiv) return null;
    for (const szene of szenen) {
      const motiv = await motivZeichnen(szene, { randFarbe: opt.randFarbe || null, zweck: opt.zweck || "bild", look });
      if (!motiv) continue;
      if (motiv.ohneRand) {
        if (archivDir) {
          try { motivAblegen(archivDir, archiv || { motive: [] }, { szene, quelle: motiv.ohneRand, datum, breite: motiv.breite, hoehe: motiv.hoehe, themaId: beitrag?.themaId || null, look, max: CONFIG.bilder.ki.archivMax }); }
          catch (e) { console.warn(`  ! Motiv nicht archiviert: ${e.message}`); }
        }
        fs.rmSync(motiv.ohneRand, { force: true });
      }
      const bild = `data:image/png;base64,${fs.readFileSync(motiv.pfad).toString("base64")}`;
      fs.rmSync(motiv.pfad, { force: true });
      return { bild, quelle: null, seite: null, frei: true, breite: motiv.breite, hoehe: motiv.hoehe, typ: look === "foto" ? "foto" : "illustration" };
    }
    console.log(`  → kein fotorealistisches KI-Motiv zu „${szenen.join("\u201c / \u201e")}".`);
    return null;
  }
  if (!CONFIG.bilder.key) return null;
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
        return { bild: `data:image/jpeg;base64,${fs.readFileSync(roh).toString("base64")}`, quelle, seite: foto.seite, frei: false, typ: "foto" };
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
      return { bild, quelle, seite: foto.seite, frei: true, breite: frei.breite || null, hoehe: frei.hoehe || null, typ: "foto" };
    }
  }
  console.log(`  → kein brauchbares Motiv zu „${szenen.join("“ / „")}“ – Titelfolie bleibt beim Icon.`);
  /* Für ein Cover gilt Foto + Icon härter als die alte ästhetische Präferenz
     gegen rechteckige Fotos: Wenn Freistellen scheitert, rettet die echte
     Fotokarte die Veröffentlichung weiterhin kostenlos. */
  if (!ersterRoh) return null;
  console.log(`  → Titelbild als Karte: „${ersteSzene}“ · ${erstesFoto.fotograf || "Pexels"}`);
  return { bild: `data:image/jpeg;base64,${fs.readFileSync(ersterRoh).toString("base64")}`, quelle: `Foto: ${erstesFoto.fotograf || "Pexels"} / Pexels`, seite: erstesFoto.seite, frei: false, typ: "foto" };
}
