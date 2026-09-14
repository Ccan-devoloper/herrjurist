/**
 * Motive zeichnen lassen statt suchen.
 *
 * Die Stockfoto-Suche hatte zwei Fehler, die sich nicht wegkonfigurieren
 * lassen: Das gefundene Foto passte oft nicht zum Thema (Atemmasken bei
 * Betrugsstrafbarkeit), und das nachträgliche Freistellen misslang häufig -
 * am 13.09. stand auf beiden Kanälen ein halbdurchsichtiger Schleier auf der
 * Kachel. Ein erzeugtes Motiv umgeht beides: Es entsteht zum Thema und kommt
 * bereits freigestellt, mit durchsichtigem Grund. Und es braucht keinen
 * Bildnachweis auf der Kachel.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { ffmpegPfad } from "./stimme.mjs";
import { CONFIG } from "./config.mjs";
import { budgetPruefen, erfassenStueck } from "./kosten.mjs";
import { alphaProfil, FESTIGKEIT_MIN, zuschneiden, bestickern, masse } from "./freistellen.mjs";

export const bildKiAktiv = () => Boolean(CONFIG.bilder.ki.aktiv && CONFIG.bilder.ki.key);

/* Der Hausstil. Zwei Dinge sind nicht verhandelbar: kein Text im Bild (Modelle
   malen Buchstaben, die wie Recht aussehen und keines sind - auf einem
   Examenskanal ein Eigentor) und genau ein Gegenstand, damit das Motiv auf der
   Kachel noch zu erkennen ist. */
/* Nennt die Szene ueberhaupt einen Menschen? Bis zum 14.09. wurde diese Frage
   nie gestellt - der Auftrag sprach immer von Armen, Haenden, Gliedmassen und
   Anatomie. Damit wurde aus "scale balancing two stacks" zuverlaessig ein
   Mensch, der neben einer Waage steht, und aus einem Reel ueber das steuerliche
   Einlagekonto eine Bilderfolge mit einem Mann und einem Einmachglas. */
const MENSCH = /\b(person|people|man|men|woman|women|someone|somebody|child|student|clerk|official|customer|client|worker|employee|judge|lawyer|defendant|witness|teacher|hand|hands|figure)\b/i;

export function bildAuftrag(szene, { stil = "" } = {}) {
  const text = String(szene).trim();
  const mitMensch = MENSCH.test(text);
  return [
    `Flat vector illustration: ${text}.`,
    "Exactly one clear subject, centred, seen from the front or in three-quarter view, nothing cropped.",
    ...(mitMensch
      /* Haende und kleine Requisiten sind die Stelle, an der billige Bilder
         auseinanderfallen: verbogene Finger, ein Stift ohne Spitze, eine Lampe,
         die keine mehr ist. Also gar nichts greifen lassen. */
      ? ["Keep the pose calm and simple: arms relaxed at the sides or lightly folded, hands open and empty.",
        "Do not let the subject hold, grip or carry anything - if the scene mentions an object, place that object on the ground or on a surface next to the subject, clearly separate from the hands.",
        "No small fiddly props, no thin stems, no objects near the face, no crossed or overlapping limbs.",
        "Correct anatomy and natural proportions."]
      /* Kein Mensch in der Szene: dann auch keinen dazuerfinden. Das Modell
         moebliert eine Szene sonst von sich aus mit einer Figur, und die Figur
         zieht dann alle Aufmerksamkeit auf sich - der Gegenstand, um den es
         geht, wird zur Requisite in ihrer Hand. */
      : ["Draw the object itself, filling the frame. Absolutely no people, no faces, no hands, no arms, no body parts, no silhouettes of persons.",
        "Show the object large, complete and instantly recognisable, at a slight angle so its shape reads clearly."]),
    "Bold simple shapes, even line weight, flat colours with soft shading, clean readable silhouette.",
    stil,
    "Absolutely no text, no letters, no words, no numbers, no signage, no logos, no watermark, no signature.",
    "No background, no ground shadow, no frame - the subject stands alone on a fully transparent background.",
  ].filter(Boolean).join(" ");
}

/**
 * Zeichnet ein Motiv und gibt es freigestellt zurück.
 * @returns {Promise<{pfad:string, breite:number, hoehe:number}|null>} null = nicht brauchbar
 */
export async function motivZeichnen(szene, { randFarbe = null, stil = "", zweck = "bild" } = {}) {
  if (!bildKiAktiv() || !szene) return null;
  budgetPruefen("Bild zeichnen");
  const ki = CONFIG.bilder.ki;
  const steuerung = new AbortController();
  const wecker = setTimeout(() => steuerung.abort(), ki.zeitlimitMs);
  let antwort;
  try {
    antwort = await fetch("https://api.openai.com/v1/images/generations", {
      method: "POST",
      headers: { Authorization: `Bearer ${ki.key}`, "Content-Type": "application/json" },
      body: JSON.stringify({ model: ki.modell, prompt: bildAuftrag(szene, { stil }), n: 1, size: ki.groesse, quality: ki.guete, background: "transparent", output_format: "png" }),
      signal: steuerung.signal,
    });
  } catch (e) {
    console.warn(`  ! Motiv zeichnen fehlgeschlagen (${e.name === "AbortError" ? "Zeitlimit" : e.message}) - Titelfolie bleibt beim Icon.`);
    return null;
  } finally { clearTimeout(wecker); }
  if (!antwort.ok) {
    const text = await antwort.text().catch(() => "");
    console.warn(`  ! Motiv zeichnen fehlgeschlagen (HTTP ${antwort.status}): ${text.slice(0, 200)}`);
    return null;
  }
  const daten = await antwort.json().catch(() => null);
  const b64 = daten?.data?.[0]?.b64_json;
  /* Bezahlt wird, sobald das Bild da ist - auch wenn es gleich verworfen wird.
     Ein Posten, der nicht gebucht wird, fehlt dem Tagesdeckel. */
  if (daten) erfassenStueck(ki.preisUsd, zweck, szene);
  if (!b64) { console.warn("  ! Motiv zeichnen: keine Bilddaten zurückgekommen."); return null; }
  const roh = path.join(os.tmpdir(), `ki-${Date.now()}-${Math.random().toString(36).slice(2, 8)}.png`);
  fs.writeFileSync(roh, Buffer.from(b64, "base64"));
  /* Dieselbe Härteprüfung wie beim Freisteller: Ein weicher Schleier ist auch
     dann ein Schleier, wenn ihn niemand ausgeschnitten hat. */
  const prof = alphaProfil(roh);
  if (!prof || prof.festigkeit < FESTIGKEIT_MIN || prof.belegt < 0.02) {
    console.warn(`  ! Gezeichnetes Motiv unbrauchbar (${prof ? `${(prof.festigkeit * 100).toFixed(0)} % deckend, ${(prof.belegt * 100).toFixed(0)} % belegt` : "kein Alphakanal"}) - Titelfolie bleibt beim Icon.`);
    fs.rmSync(roh, { force: true });
    return null;
  }
  const geschnitten = zuschneiden(roh);
  /* Eine randlose Kopie fuers Archiv: Der farbige Rand haengt am Rechtsgebiet
     und wird bei jeder Verwendung neu gezogen. */
  const ohneRand = geschnitten.replace(/\.png$/, "-roh.png");
  fs.copyFileSync(geschnitten, ohneRand);
  const fertig = randFarbe ? bestickern(geschnitten, randFarbe) : geschnitten;
  const m = masse(fertig) || {};
  console.log(`  → Motiv gezeichnet: „${szene}" (${(prof.festigkeit * 100).toFixed(0)} % deckend)`);
  return { pfad: fertig, ohneRand, breite: m.breite || null, hoehe: m.hoehe || null };
}

/**
 * Holt ein archiviertes Motiv hervor und zieht den Rand in der heutigen Farbe.
 * @returns {{pfad:string, breite:number, hoehe:number}|null}
 */
export function motivHervorholen(quelle, { randFarbe = null } = {}) {
  if (!fs.existsSync(quelle)) return null;
  const kopie = path.join(os.tmpdir(), `archiv-${Date.now()}-${Math.random().toString(36).slice(2, 8)}.png`);
  /* Der Rand wird auf einem PNG gezogen; ein archiviertes WebP muss dafuer
     zurueckverwandelt werden. */
  if (/\.webp$/i.test(quelle)) {
    const s = spawnSync(ffmpegPfad(), ["-y", "-loglevel", "error", "-i", quelle, "-frames:v", "1", "-update", "1", kopie], { encoding: "utf8", timeout: 60000 });
    if (s.status !== 0 || !fs.existsSync(kopie)) { console.warn("  ! Archiviertes Motiv nicht lesbar."); return null; }
  } else fs.copyFileSync(quelle, kopie);
  const fertig = randFarbe ? bestickern(kopie, randFarbe) : kopie;
  const m = masse(fertig) || {};
  return { pfad: fertig, breite: m.breite || null, hoehe: m.hoehe || null };
}
