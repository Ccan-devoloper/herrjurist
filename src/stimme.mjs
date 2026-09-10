/* ==========================================================================
   Sprecherstimme für Reels – drei Anbieter, automatisch gewählt:

     elevenlabs  natürlichste Stimme (Modell eleven_v3), liefert Wort-Zeitmarken.
                 Aktiv, wenn ELEVENLABS_API_KEY gesetzt und das Monatskontingent
                 des Abos noch reicht.
     piper       kostenlos, offline, neuronale Stimme „Thorsten“ (de_DE-thorsten-high).
                 Läuft im GitHub-Runner; Modell wird beim ersten Lauf geladen.
     pico        kostenlos, offline, SVOX Pico (apt: libttspico-utils). Deutlich
                 hörbar synthetisch – nur Notlösung und für Tests.
     aus         stumm mit geschätzter Dauer (Storyboard-Tests).

   Kontingent: Das kostenlose ElevenLabs-Abo hat 10 000 Zeichen im Monat. Der
   Bot fragt vor jedem Reel das verbleibende Guthaben ab und nimmt ElevenLabs
   nur, wenn es für das ganze Reel reicht – sonst spricht Piper. Innerhalb
   eines Reels wird die Stimme nie gewechselt, das hört jeder. Ist das
   Kontingent aufgebraucht, merkt sich der Bot das bis zum Stichtag des Abos
   (state/stimme.json) und fragt nicht bei jedem Lauf erneut nach.

   IG_STIMME erzwingt einen Anbieter. Alle Anbieter liefern je Szene eine
   Audiodatei, die Dauer und Wortzeiten für die Untertitel. Bei piper/pico
   wird satzweise synthetisiert, damit die Untertitel je Satz sauber sitzen.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { execFileSync, spawnSync } from "node:child_process";
import { CONFIG } from "./config.mjs";

export function ffmpegPfad() {
  return process.env.FFMPEG_PATH || "ffmpeg";
}

function vorhanden(befehl) {
  return spawnSync("sh", ["-c", `command -v ${befehl}`], { stdio: "ignore" }).status === 0;
}

/* Dauer einer Audiodatei in Sekunden (über ffmpeg, ohne ffprobe-Abhängigkeit). */
export function audioDauer(datei) {
  const r = spawnSync(ffmpegPfad(), ["-hide_banner", "-i", datei, "-f", "null", "-"], { encoding: "utf8" });
  const m = String(r.stderr || "").match(/time=(\d+):(\d+):(\d+\.\d+)/g);
  if (!m) return 0;
  const [, h, mi, s] = m[m.length - 1].match(/time=(\d+):(\d+):(\d+\.\d+)/);
  return Number(h) * 3600 + Number(mi) * 60 + Number(s);
}

/* Geschätzte Sprechdauer: ca. 15 Zeichen je Sekunde bei ruhigem Tempo. */
export function sprechdauerSchaetzen(text) {
  const zeichen = String(text).replace(/\s+/g, " ").trim().length;
  return Math.max(1.4, zeichen / 15 + 0.4);
}

/* Wörter gewichtet nach Länge über eine Dauer verteilen. */
export function woerterVerteilen(text, dauer, start = 0) {
  const woerter = String(text).split(/\s+/).filter(Boolean);
  const gewichte = woerter.map((w) => w.length + 2);
  const summe = gewichte.reduce((a, b) => a + b, 0);
  let t = start;
  return woerter.map((w, i) => { const d = (gewichte[i] / summe) * dauer; const o = { wort: w, von: t, bis: t + d }; t += d; return o; });
}

export function saetze(text) {
  return String(text).replace(/\s+/g, " ").trim().split(/(?<=[.!?…])\s+(?=[„"A-ZÄÖÜ0-9])/).filter(Boolean);
}

/* --- Kontingent des ElevenLabs-Abos -------------------------------------
   Der Stand liegt im Assets-Zweig (state/stimme.json), damit ein Lauf vom
   vorherigen weiß. lauf.mjs reicht Lese- und Schreibfunktion herein; ohne
   Anbindung arbeitet das Modul nur im Arbeitsspeicher (Tests, Trockenläufe). */
let standSpeicher = null;
let standCache = null;
let restCache = null;          // im Lauf einmal abgefragtes Restguthaben

export function stimmeStandVerbinden(speicher = null) {
  standSpeicher = speicher;
  standCache = null;
  restCache = null;
}

const LEER = () => ({ verbraucht: 0, grenze: null, rest: null, erschoepft: false, abo: null, resetAm: null });

export function stimmeStand() {
  if (standCache) return standCache;
  let roh = null;
  try { roh = standSpeicher?.lesen?.() || null; } catch { roh = null; }
  standCache = { ...LEER(), ...(roh || {}) };
  /* Am Stichtag des Abos füllt ElevenLabs das Guthaben wieder auf – dann gilt
     der gemerkte Ausfall nicht mehr. */
  if (standCache.erschoepft && standCache.resetAm && new Date(standCache.resetAm) <= new Date()) standCache = { ...LEER(), abo: standCache.abo };
  return standCache;
}

function standSchreiben(aenderung) {
  standCache = { ...stimmeStand(), ...aenderung, stand: new Date().toISOString() };
  try { standSpeicher?.schreiben?.(standCache); } catch (e) { console.warn(`  ! Stimmen-Stand nicht gespeichert: ${e.message}`); }
  return standCache;
}

/* Verbrauch je Zeichen: die schnellen Modelle kosten das halbe Guthaben. */
const kreditFaktor = () => (/flash|turbo/i.test(CONFIG.reel.modell || "") ? 0.5 : 1);

/* Quotenfehler erkennen: ElevenLabs meldet ein leeres Kontingent je nach
   Endpunkt mit 401 (quota_exceeded) oder 429. Ein ungültiger Schlüssel meldet
   ebenfalls 401 – der darf den Monat nicht als verbraucht markieren, deshalb
   zählt nur der Wortlaut der Antwort. */
function istKontingentFehler(fehler) {
  return /quota_exceeded|quota|insufficient|ElevenLabs 429/i.test(String(fehler?.message || fehler));
}

/** Restguthaben des Monats in Zeichen; null, wenn es sich nicht ermitteln lässt. */
export async function kontingentAbfragen({ frisch = false } = {}) {
  const key = CONFIG.reel.elevenlabsKey;
  if (!key) return null;
  if (!frisch && restCache != null) return restCache;
  try {
    const res = await fetch("https://api.elevenlabs.io/v1/user/subscription", { headers: { "xi-api-key": key } });
    if (!res.ok) {
      const text = (await res.text()).slice(0, 200);
      console.warn(`  ! ElevenLabs-Kontingent nicht abrufbar (${res.status}): ${text}`);
      return null;
    }
    const j = await res.json();
    const grenze = Number(j.character_limit || 0);
    const verbraucht = Number(j.character_count || 0);
    const rest = Math.max(0, grenze - verbraucht);
    const resetAm = j.next_character_count_reset_unix ? new Date(j.next_character_count_reset_unix * 1000).toISOString() : null;
    standSchreiben({ verbraucht, grenze, rest, abo: j.tier || null, resetAm, erschoepft: rest <= 0 });
    restCache = rest;
    return rest;
  } catch (e) {
    console.warn(`  ! ElevenLabs-Kontingent nicht abrufbar: ${e.message}`);
    return null;
  }
}

/* Stimmen, die dieses Konto nicht sprechen darf (Bibliotheksstimme im
   kostenlosen Abo, HTTP 402). Der Lauf merkt sie sich und wirft sie aus der
   Kandidatenliste – sonst fällt jedes Reel still auf Piper zurück. */
const gesperrteStimmen = new Set();
export const stimmeIstGesperrt = (id) => gesperrteStimmen.has(id);
const istTarifFehler = (fehler) => /paid_plan_required|library voices/i.test(String(fehler?.message || fehler));

/* Kontingent für diesen Lauf als aufgebraucht vermerken. */
function kontingentErschoepft(grund = "") {
  restCache = 0;
  standSchreiben({ rest: 0, erschoepft: true, grund: grund.slice(0, 200) });
  console.log(`  → ElevenLabs-Kontingent aufgebraucht${grund ? ` (${grund})` : ""} – ab jetzt spricht ${offlineAnbieter()}.`);
}

/* Verbrauchte Zeichen mitschreiben, damit der Stand auch ohne erneute Abfrage
   stimmt (und der nächste Reel-Check nicht in die Quote läuft). */
function verbrauchBuchen(text) {
  const zeichen = Math.ceil(String(text).length * kreditFaktor());
  const s = stimmeStand();
  const rest = s.rest == null ? null : Math.max(0, s.rest - zeichen);
  if (restCache != null) restCache = Math.max(0, restCache - zeichen);
  standSchreiben({ verbraucht: (s.verbraucht || 0) + zeichen, rest, erschoepft: rest === 0 });
}

/* Welcher kostenlose Anbieter steht bereit? */
export function offlineAnbieter() {
  if (vorhanden("piper") && piperModell()) return "piper";
  if (vorhanden("pico2wave")) return "pico";
  return "aus";
}

/* Welcher Anbieter läuft? Ohne frische Abfrage – nur nach gemerktem Stand. */
export function stimmenAnbieter() {
  const wunsch = (process.env.IG_STIMME || "").toLowerCase();
  if (wunsch) return wunsch;
  if (CONFIG.reel.elevenlabsKey && !stimmeStand().erschoepft) return "elevenlabs";
  return offlineAnbieter();
}

/**
 * Anbieter für ein ganzes Reel: ElevenLabs nur, wenn das Monatsguthaben den
 * kompletten Sprechertext trägt. Reicht es nicht mehr, spricht von der ersten
 * Szene an die Offline-Stimme – ein Wechsel mitten im Video wäre hörbar.
 * @param {number} zeichen Länge aller Sprechertexte des Reels
 */
export async function anbieterFuerText(zeichen = 0) {
  const wunsch = (process.env.IG_STIMME || "").toLowerCase();
  if (wunsch) return wunsch;
  if (!CONFIG.reel.elevenlabsKey) return offlineAnbieter();
  if (stimmeStand().erschoepft) return offlineAnbieter();
  const rest = await kontingentAbfragen();
  /* Kein Zugriff auf den Kontostand (Netz, Wartung): ElevenLabs versuchen,
     der Quotenfehler fängt es unten ab. */
  if (rest == null) return "elevenlabs";
  const noetig = Math.ceil(zeichen * kreditFaktor());
  if (noetig > rest) {
    if (rest <= 0) kontingentErschoepft("Monatsguthaben verbraucht");
    else console.log(`  → ElevenLabs: ${rest} von ${stimmeStand().grenze ?? "?"} Zeichen frei, das Reel braucht ${noetig} – es spricht ${offlineAnbieter()}.`);
    return offlineAnbieter();
  }
  console.log(`  → ElevenLabs: ${rest} Zeichen frei${stimmeStand().abo ? ` (Abo ${stimmeStand().abo})` : ""}, das Reel braucht ${noetig}.`);
  return "elevenlabs";
}

function piperModell() {
  const dir = process.env.PIPER_VOICES_DIR || path.resolve(process.env.HOME || "/tmp", ".cache/piper-voices");
  const name = process.env.PIPER_VOICE || "de_DE-thorsten-high";
  const onnx = path.join(dir, `${name}.onnx`);
  return fs.existsSync(onnx) && fs.existsSync(`${onnx}.json`) ? onnx : null;
}

/* --- ElevenLabs --------------------------------------------------------- */
function alignmentZuWoertern(alignment, start) {
  const zeichen = alignment.characters || [];
  const anfang = alignment.character_start_times_seconds || [];
  const ende = alignment.character_end_times_seconds || [];
  const woerter = [];
  let aktuell = null;
  for (let i = 0; i < zeichen.length; i++) {
    const c = zeichen[i];
    if (/\s/.test(c)) { if (aktuell) { woerter.push(aktuell); aktuell = null; } continue; }
    if (!aktuell) aktuell = { wort: c, von: start + anfang[i], bis: start + ende[i] };
    else { aktuell.wort += c; aktuell.bis = start + ende[i]; }
  }
  if (aktuell) woerter.push(aktuell);
  return woerter.length ? woerter : null;
}

async function elevenlabs(text, zielDatei, art = "normal", stimmeId = null) {
  const key = CONFIG.reel.elevenlabsKey;
  const id = stimmeId || CONFIG.reel.stimme;
  if (!id) throw new Error("Keine ElevenLabs-Stimme gewählt (ELEVENLABS_VOICE_ID oder state/stimmen.json)");
  const url = `https://api.elevenlabs.io/v1/text-to-speech/${encodeURIComponent(id)}/with-timestamps?output_format=mp3_44100_128`;
  const res = await fetch(url, {
    method: "POST",
    headers: { "xi-api-key": key, "Content-Type": "application/json" },
    body: JSON.stringify({ text, model_id: CONFIG.reel.modell, language_code: "de", voice_settings: art === "hook"
      /* Weniger Stabilität und mehr Stil heißt bei ElevenLabs: lebendiger,
         mit stärkerer Betonung – genau das, was der Aufhänger braucht. */
      ? { stability: 0.32, similarity_boost: 0.8, style: 0.6, use_speaker_boost: true, speed: 0.97 }
      : { stability: 0.45, similarity_boost: 0.8, style: 0.35, use_speaker_boost: true, speed: 1.0 } }),
  });
  if (!res.ok) throw new Error(`ElevenLabs ${res.status}: ${(await res.text()).slice(0, 200)}`);
  const json = await res.json();
  fs.writeFileSync(zielDatei, Buffer.from(json.audio_base64, "base64"));
  const dauer = audioDauer(zielDatei) || sprechdauerSchaetzen(text);
  const woerter = alignmentZuWoertern(json.alignment || json.normalized_alignment || {}, 0) || woerterVerteilen(text, dauer);
  return { datei: zielDatei, dauer, woerter, echt: true, anbieter: "elevenlabs", stimmeId: id };
}

/* Betonung: Der Hook wird bewusst anders gesprochen als der Rest – etwas
   langsamer, mit längerer Pause am Satzende und einen Tick lauter. Eine
   Offline-Stimme kann nicht schauspielern; Tempo, Pause und Lautheit sind die
   Stellschrauben, die sie hat. */
const BETONUNG = {
  hook: { tempo: 1.07, satzpause: "0.35", lautheit: -15.5 },
  normal: { tempo: 1.0, satzpause: "0.15", lautheit: -17 },
};

/* --- Offline-Anbieter: satzweise synthetisieren, dann zusammensetzen ------ */
function satzSynthese(anbieter, satz, wav, art = "normal") {
  const b = BETONUNG[art] || BETONUNG.normal;
  if (anbieter === "piper") {
    const tempo = process.env.PIPER_TEMPO ? Number(process.env.PIPER_TEMPO) * (b.tempo / BETONUNG.normal.tempo) : b.tempo;
    const r = spawnSync("piper", ["-m", piperModell(), "-f", wav, "--length-scale", String(tempo), "--sentence-silence", b.satzpause], { input: satz, encoding: "utf8" });
    if (r.status !== 0) throw new Error(`piper: ${r.stderr}`);
  } else if (anbieter === "pico") {
    const r = spawnSync("pico2wave", ["-l", "de-DE", "-w", wav, satz], { encoding: "utf8" });
    if (r.status !== 0) throw new Error(`pico2wave: ${r.stderr}`);
  } else throw new Error(`Unbekannter Stimmanbieter ${anbieter}`);
}

function offline(anbieter, text, zielDatei, art = "normal") {
  const b = BETONUNG[art] || BETONUNG.normal;
  const teile = saetze(text);
  const dir = path.dirname(zielDatei);
  const basis = path.basename(zielDatei, path.extname(zielDatei));
  const pause = 0.22;
  const wavs = [];
  const woerter = [];
  let t = 0;
  teile.forEach((satz, i) => {
    const wav = path.join(dir, `${basis}-s${i}.wav`);
    satzSynthese(anbieter, satz, wav, art);
    const d = audioDauer(wav);
    const dEff = anbieter === "pico" ? d / 1.1 : d;   // Pico wird um 10 % gestrafft
    woerter.push(...woerterVerteilen(satz, Math.max(0.2, dEff - 0.1), t));
    wavs.push({ wav, d: dEff });
    t += dEff + pause;
  });
  /* Sätze mit kurzen Pausen aneinanderhängen, leicht entrauschen und angleichen. */
  const liste = path.join(dir, `${basis}-liste.txt`);
  const stille = path.join(dir, `${basis}-pause.wav`);
  execFileSync(ffmpegPfad(), ["-y", "-loglevel", "error", "-f", "lavfi", "-i", `anullsrc=r=16000:cl=mono`, "-t", String(pause), stille]);
  fs.writeFileSync(liste, wavs.flatMap((w, i) => [`file '${w.wav}'`, ...(i < wavs.length - 1 ? [`file '${stille}'`] : [])]).join("\n"));
  execFileSync(ffmpegPfad(), ["-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", liste, "-af", `${anbieter === "pico" ? "atempo=1.1," : ""}aresample=44100,highpass=f=80,loudnorm=I=${b.lautheit}:TP=-1.5:LRA=9`, "-c:a", "libmp3lame", "-q:a", "3", zielDatei]);
  for (const w of wavs) fs.rmSync(w.wav, { force: true });
  fs.rmSync(liste, { force: true }); fs.rmSync(stille, { force: true });
  const dauer = audioDauer(zielDatei) || t;
  return { datei: zielDatei, dauer, woerter, echt: true, anbieter };
}

/**
 * Spricht einen Text. Rückgabe: { datei (mp3|null), dauer, woerter:[{wort,von,bis}], echt, anbieter }
 */
export async function sprechen(text, zielDatei, opt = {}) {
  const anbieter = opt.anbieter || stimmenAnbieter();
  const art = opt.betonung === "hook" ? "hook" : "normal";
  fs.mkdirSync(path.dirname(zielDatei), { recursive: true });
  if (anbieter === "elevenlabs") {
    try {
      const ergebnis = await elevenlabs(text, zielDatei, art, opt.stimmeId || null);
      verbrauchBuchen(text);
      return ergebnis;
    } catch (e) {
      /* Guthaben mitten im Lauf leer: nicht abbrechen – das Reel soll täglich
         erscheinen. Der Rest des Monats läuft dann über die Offline-Stimme. */
      if (istKontingentFehler(e)) kontingentErschoepft(e.message);
      else if (istTarifFehler(e)) {
        const id = opt.stimmeId || CONFIG.reel.stimme;
        gesperrteStimmen.add(id);
        console.warn(`  ! Diese Stimme darf das Abo nicht über die API sprechen (Bibliotheksstimme im kostenlosen Tarif) – sie fliegt aus der Auswahl.`);
      } else console.warn(`  ! ElevenLabs antwortet nicht (${e.message}) – diese Szene spricht ${offlineAnbieter()}.`);
      return sprechen(text, zielDatei, { ...opt, anbieter: offlineAnbieter() });
    }
  }
  if (anbieter === "piper" || anbieter === "pico") return offline(anbieter, text, zielDatei, art);
  const dauer = sprechdauerSchaetzen(text);
  return { datei: null, dauer, woerter: woerterVerteilen(text, dauer), echt: false, anbieter: "aus" };
}
