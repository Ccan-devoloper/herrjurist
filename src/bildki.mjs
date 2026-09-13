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
import { CONFIG } from "./config.mjs";
import { budgetPruefen, erfassenStueck } from "./kosten.mjs";
import { alphaProfil, FESTIGKEIT_MIN, zuschneiden, bestickern, masse } from "./freistellen.mjs";

export const bildKiAktiv = () => Boolean(CONFIG.bilder.ki.aktiv && CONFIG.bilder.ki.key);

/* Der Hausstil. Zwei Dinge sind nicht verhandelbar: kein Text im Bild (Modelle
   malen Buchstaben, die wie Recht aussehen und keines sind - auf einem
   Examenskanal ein Eigentor) und genau ein Gegenstand, damit das Motiv auf der
   Kachel noch zu erkennen ist. */
export function bildAuftrag(szene, { stil = "" } = {}) {
  return [
    `Flat vector illustration: ${String(szene).trim()}.`,
    "Exactly one clear subject, centred, seen from a slight angle, nothing cropped.",
    "Bold simple shapes, soft shading, warm friendly palette, thick clean outlines, modern editorial style.",
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
  const fertig = randFarbe ? bestickern(geschnitten, randFarbe) : geschnitten;
  const m = masse(fertig) || {};
  console.log(`  → Motiv gezeichnet: „${szene}" (${(prof.festigkeit * 100).toFixed(0)} % deckend)`);
  return { pfad: fertig, breite: m.breite || null, hoehe: m.hoehe || null };
}
