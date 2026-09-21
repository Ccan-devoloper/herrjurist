/* global FormData, Blob */
/**
 * Wiederkehrende Herr-Jurist-Charaktere als thematische Cover- und Reel-Szenen.
 *
 * Anders als die fruehere Stockfoto-/Einzelmotiv-Pipeline entstehen hier keine
 * austauschbaren Gegenstaende. Je nach Inhalt werden eine, zwei oder mehrere
 * feste Figuren aus ihren Referenzbildern in eine neue, zum juristischen Thema
 * passende Handlung gesetzt. Requisiten sind kein Muss: Entscheidend ist, dass
 * die Szene den juristischen Gedanken sofort sichtbar macht.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { execFileSync } from "node:child_process";
import { CONFIG } from "./config.mjs";
import { ffmpegPfad } from "./stimme.mjs";
import { bildAufruf, openaiBildEditSenden } from "./anbieter.mjs";
import { alphaProfil, FESTIGKEIT_MIN, zuschneiden, bestickern, masse, randkontakt, randVerdacht, freistellen } from "./freistellen.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const basis = path.resolve(hier, "../assets/charaktere");

export const CHARAKTERE = Object.freeze({
  rex: {
    id: "rex", name: "Rex Rohrbruch", datei: "rex-rohrbruch.jpg.b64",
    kurz: "lanky light-skinned anxious male portal mechanic with messy brown hair, patched blue-grey work suit, brown boots, tool backpack and traces of green portal fluid",
  },
  zylla: {
    id: "zylla", name: "Zylla Glitch", datei: "zylla-glitch.jpg.b64",
    kurz: "slim green-skinned alien woman with magenta swept hair, two antennae, oversized lavender iridescent jacket, black top, black skinny trousers and pink-white sneakers",
  },
  form7: {
    id: "form7", name: "FORM-7", datei: "form-7.jpg.b64",
    kurz: "floating pale-blue round-headed bureaucratic drone with sleepy half-lidded eyes, dark side panels, a small gold antenna-crown, white-gold uniform torso, clipboard and tiny side pods",
  },
  brakk: {
    id: "brakk", name: "Brakk Quarzfaust", datei: "brakk-quarzfaust.jpg.b64",
    kurz: "very muscular tan miner with a square jaw, purple-blue crystal growths on shoulders and head, miner headlamp, brown bib overalls, heavy grey boots and gloves",
  },
  flux: {
    id: "flux", name: "Prof. Wurmfried Flux", datei: "prof-wurmfried-flux.jpg.b64",
    kurz: "tall pink segmented worm-like professor with large round glasses, sparse hair, cheerful face, white-gold academic tunic, pointer and round hover base",
  },
  mara: {
    id: "mara", name: "Mara Sternpfad", datei: "mara-sternpfad.jpg.b64",
    kurz: "older light-skinned woman with grey hair in a messy bun, yellow cap, cigarette, orange vest over black top, olive cargo trousers and a large green expedition backpack with antenna dish and many pouches",
  },
});

export function charakterBildAktiv() {
  return Boolean(CONFIG.bilder?.charaktere?.aktiv && CONFIG.bilder?.ki?.key);
}

function zielText(ziel = {}) {
  const titel = ziel?.folien?.find?.((f) => f.art === "titel")?.titel || "";
  return [
    ziel.kurztitel, ziel.fachLabel, ziel.fach, ziel.format, titel,
    ziel.titel, ziel.unter, ziel.text, ziel.sprecher, ziel.norm,
    ziel.bildSzene, ziel.bildSzeneAlt, ziel.coverText,
    ...(Array.isArray(ziel.coverCharaktere) ? ziel.coverCharaktere : []),
  ].filter(Boolean).join(" · ");
}

const REGELN = [
  /* Fallback nur fuer Altbestand ohne strukturierte Cover-Regie. Neue Inhalte
     liefern coverCharaktere direkt aus dem Autoren-Aufruf. Die Regeln duerfen
     bewusst 1, 2 oder 3 Figuren liefern. */
  { re: /142|unfall|unfallort|verkehrsunfall|flucht/i, ids: ["rex", "mara"] },
  { re: /versuch|unmittelbar|letzten handgriff/i, ids: ["rex", "mara"] },
  { re: /besitz|eigentum/i, ids: ["brakk", "form7"] },
  { re: /anfecht|irrtum|kausal/i, ids: ["form7", "rex"] },
  { re: /angebot|annahme|schaufenster|invitatio/i, ids: ["form7", "zylla"] },
  { re: /kuendig|kündig|zugang|fristbeginn/i, ids: ["zylla", "flux"] },
  { re: /vollzieh|aufschieb|80 abs|verwalt|vwgo|bescheid/i, ids: ["mara", "form7"] },
  { re: /mittaeter|mittäter|mehrpersonen|dreiperson|vertretung/i, ids: ["brakk", "zylla", "form7"] },
  { re: /definition|begriff|dogmatik/i, ids: ["flux"] },
  { re: /mindset|blackout|zeitdruck|perfektion/i, ids: ["mara"] },
  { re: /schema|pruef|prüf|aufbau|zulaess|zuläss|begruendet|begründet|klausur|methodik/i, ids: ["form7", "flux"] },
  { re: /straf|tatbestand|diebstahl|raub|koerper|körper|gewalt/i, ids: ["brakk", "form7"] },
  { re: /erbe|testament|famil|nachlass|erbrecht/i, ids: ["mara", "flux"] },
  { re: /sache|mangel|schaden|werk|repar|bau|kauf|liefer/i, ids: ["rex", "brakk"] },
];

function idsAusRegie(ziel = {}) {
  const roh = ziel.coverCharaktere || ziel?.folien?.find?.((f) => f.art === "titel")?.coverCharaktere;
  if (!Array.isArray(roh)) return [];
  return [...new Set(roh.map((x) => String(x || "").toLowerCase()).filter((id) => CHARAKTERE[id]))].slice(0, 6);
}

export function charaktereFuer(ziel = {}) {
  const vorgegeben = idsAusRegie(ziel);
  if (vorgegeben.length) return vorgegeben.map((id) => CHARAKTERE[id]);
  const text = zielText(ziel);
  for (const regel of REGELN) if (regel.re.test(text)) return regel.ids.map((id) => CHARAKTERE[id]);
  return [CHARAKTERE.form7, CHARAKTERE.flux];
}

function handlungFuer(ziel, chars) {
  const text = zielText(ziel);
  const a = chars[0]?.name || "the character";
  const b = chars[1]?.name || "another character";
  const c = chars[2]?.name || "a third character";
  const gruppe = chars.map((x) => x.name).join(", ");
  if (/kuendig|kündig/i.test(text)) return `${a} hands ${b} a blank termination letter; ${b} reacts surprised while ${a} clearly ends the relationship.`;
  if (/142|unfall|unfallort|24 stunden/i.test(text)) return `${a} turns away from a lightly damaged small car as if leaving the accident scene, while ${b} stops them and points back to the car.`;
  if (/streit|ansicht|ergebnis|vergleich/i.test(text)) return `${a} carefully compares two different blank solution sheets side by side while ${b} waits before starting an argument.`;
  if (/anfecht|irrtum/i.test(text)) return `${a} points out an obvious mistake on a blank contract while ${b} suddenly realizes the error.`;
  if (/angebot|annahme|vertragsschluss|schaufenster/i.test(text)) return `${a} presents a blank offer sheet while ${b} deliberately decides whether to accept it.`;
  if (/besitz|eigentum/i.test(text)) return `${a} holds a house key while ${b} points to a separate blank ownership document, making clear that possession and ownership are different.`;
  if (/versuch|letzten handgriff|unmittelbar/i.test(text)) return `${a} is just about to complete a decisive action while ${b} stops and examines the moment immediately before completion.`;
  if (/zulaess|zuläss|begruendet|begründet/i.test(text)) return `${a} checks a first procedural gate on a blank checklist before allowing ${b} to move to a clearly separate second stage.`;
  if (/vollzieh|aufschieb/i.test(text)) return `${a} checks whether a process is already running before ${b} reaches for a large pause switch.`;
  if (/frist|kalender|zugang/i.test(text)) return `${a} points at a blank calendar while ${b} holds a sealed blank envelope, both concentrating on the correct timing.`;
  if (/dieb|raub|straf|tatbestand/i.test(text)) return `${a} reenacts the concrete act while ${b} inspects the sequence step by step.`;
  const cue = String(ziel?.bildSzene || ziel?.titel || ziel?.kurztitel || "a legal exam problem").trim();
  if (chars.length === 1) return `${a} acts out this concrete exam situation in one immediately readable pose: ${cue}.`;
  if (chars.length >= 3) return `${gruppe} form one coherent interaction that makes this concrete exam situation instantly understandable: ${cue}.`;
  return `${a} and ${b} act out this concrete exam situation: ${cue}. Their interaction, not mere posing, must communicate the point.`;
}

export function charakterPrompt(ziel = {}, chars = charaktereFuer(ziel)) {
  const referenzen = chars.map((c, i) =>
    `Reference image ${i + 1} is ${c.name}: ${c.kurz}. Preserve this exact character identity, face, body proportions, outfit, colours and distinctive features.`
  ).join(" ");
  const kontext = zielText(ziel).slice(0, 1100);
  const handlung = handlungFuer(ziel, chars);
  return [
    "Create a NEW flat 2D sci-fi comedy cartoon vignette using the supplied recurring character reference image(s).",
    referenzen,
    "Use exactly the selected recurring characters. The selection may contain one or more characters, up to the six supplied recurring identities; do not invent extra people or duplicate a character.",
    "Do not copy the reference poses. Redraw the same identities in a new, topic-specific interaction.",
    `Scene action: ${handlung}`,
    `Legal-topic context, only to understand the visual meaning: ${kontext}`,
    "Choose props by meaning, not by formula. Use no prop when gesture alone explains the point; use one or more clearly relevant objects when they make the legal distinction immediately understandable.",
    "Build one coherent scene, not separate portraits. Characters may stand on either side of a central object, overlap naturally, point, hand things over, stop each other, compare documents or demonstrate a sequence.",
    "Make the vignette visually substantial: the complete scene should occupy roughly 85 to 92 percent of the usable canvas width or height while still keeping every head, hand, foot and essential prop fully visible.",
    "Keep silhouettes readable at Instagram thumbnail size. Exaggerate gesture and facial reaction enough that the action is understood before reading the caption.",
    "Do not render explanatory prose inside the illustration. Documents, screens and signs should stay blank or use simple abstract marks; a short deterministic callout, when useful, is added later by the Herrjurist renderer so spelling stays correct.",
    "No background and no scenery: transparent background, no room, no landscape and no decorative frame. Ground shadows that belong directly under the characters or object are allowed.",
    "Use only a modest transparent safety margin around the complete vignette; do not shrink the scene into a small sticker in one corner.",
    "Bold clean outlines, flat colours, subtle simple shading, consistent with the supplied original character artwork.",
  ].join(" ");
}

export function bildKostenUsd(antwort) {
  const u = antwort?.usage;
  if (!u) return null;
  const d = u.input_tokens_details || {};
  const od = u.output_tokens_details || {};
  const bildEin = Number(d.image_tokens || 0);
  const textEin = Number(d.text_tokens || Math.max(0, Number(u.input_tokens || 0) - bildEin));
  const bildAus = Number(od.image_tokens || u.output_tokens || 0);
  const textAus = Number(od.text_tokens || 0);
  const usd = bildEin * 8 / 1e6 + textEin * 5 / 1e6 + bildAus * 30 / 1e6 + textAus * 10 / 1e6;
  return Number(usd.toFixed(6));
}

function referenzNormalisieren(char) {
  const quelle = path.join(basis, char.datei);
  const b64 = fs.readFileSync(quelle, "utf8").trim();
  const roh = path.join(os.tmpdir(), `hj-ref-${char.id}-${process.pid}-${Date.now()}.jpg`);
  const norm = path.join(os.tmpdir(), `hj-ref-${char.id}-${process.pid}-${Date.now()}-384.jpg`);
  fs.writeFileSync(roh, Buffer.from(b64, "base64"));
  try {
    /* Die ersten Testreferenzen waren extrem kleine Thumbnails. GPT Image
       lehnt solche Dateien als ungueltige Bildeingabe ab. Vor jedem Upload
       werden sie daher in ein echtes 384x384-JPEG mit weissem Rand
       normalisiert; der Charakter selbst wird dabei nicht veraendert. */
    execFileSync(ffmpegPfad(), [
      "-y", "-loglevel", "error", "-i", roh,
      "-vf", "scale=336:336:force_original_aspect_ratio=decrease,pad=384:384:(ow-iw)/2:(oh-ih)/2:color=white",
      "-frames:v", "1", "-q:v", "3", norm,
    ]);
    return norm;
  } finally {
    fs.rmSync(roh, { force: true });
  }
}

const schlafen = (ms) => new Promise((r) => setTimeout(r, ms));
let letzterBildStart = 0;

async function ratenfensterWarten(ms = 13000) {
  const warten = Math.max(0, letzterBildStart + ms - Date.now());
  if (warten > 0) await schlafen(warten);
  letzterBildStart = Date.now();
}

async function editAufruf({ chars, prompt, quality, size, key, modell, zeitlimitMs }) {
  const refs = chars.map(referenzNormalisieren);
  try {
    for (let rateVersuch = 0; rateVersuch < 3; rateVersuch++) {
      const form = new FormData();
      form.append("model", modell);
      refs.forEach((datei, i) => {
        const bytes = fs.readFileSync(datei);
        form.append("image[]", new Blob([bytes], { type: "image/jpeg" }), `${chars[i].id}.jpg`);
      });
      form.append("prompt", prompt);
      form.append("quality", quality);
      form.append("size", size);
      form.append("background", "transparent");
      form.append("output_format", "png");
      try {
        /* Tier 1 erlaubt fuer GPT Image derzeit nur wenige Bilder pro Minute.
           Auch ein erfolgreicher Aufruf zaehlt; deshalb nicht erst nach 429
           bremsen, sondern jeden Bildstart bewusst auseinanderziehen. */
        await ratenfensterWarten(Number(CONFIG.bilder?.charaktere?.minAbstandMs || 13000));
        return await openaiBildEditSenden({ form, key, zeitlimitMs });
      } catch (fehler) {
        if (Number(fehler?.status) !== 429 || rateVersuch === 2) throw fehler;
        const retry = Number(fehler?.retryAfter || 0);
        const warten = Math.max(13000, Number.isFinite(retry) ? retry * 1000 : 0);
        console.warn(`  ! GPT-Image-Ratenlimit; ${Math.ceil(warten / 1000)} s Pause, dann gleicher Versuch erneut.`);
        await schlafen(warten);
      }
    }
    throw new Error("GPT-Image-Ratenlimit nach drei Versuchen");
  } finally {
    for (const p of refs) fs.rmSync(p, { force: true });
  }
}

function dateiAusAntwort(daten) {
  const b64 = daten?.data?.[0]?.b64_json;
  if (!b64) return null;
  const roh = path.join(os.tmpdir(), `charakter-${Date.now()}-${Math.random().toString(36).slice(2, 8)}.png`);
  fs.writeFileSync(roh, Buffer.from(b64, "base64"));
  return roh;
}

function qa(roh, randFarbe = null) {
  let arbeitsPfad = roh;
  let prof = alphaProfil(arbeitsPfad);
  const alphaTaugt = prof && prof.festigkeit >= FESTIGKEIT_MIN && prof.belegt >= 0.02;
  if (!alphaTaugt) {
    const frei = freistellen(arbeitsPfad, { randFarbe: null, schaerfePruefen: false });
    fs.rmSync(arbeitsPfad, { force: true });
    if (!frei?.pfad) return null;
    arbeitsPfad = frei.pfad;
    prof = alphaProfil(arbeitsPfad);
  }
  if (!prof || prof.festigkeit < FESTIGKEIT_MIN || prof.belegt < 0.02) {
    fs.rmSync(arbeitsPfad, { force: true });
    return null;
  }
  const randFehler = randVerdacht(randkontakt(arbeitsPfad));
  if (randFehler) {
    fs.rmSync(arbeitsPfad, { force: true });
    return null;
  }
  const geschnitten = zuschneiden(arbeitsPfad);
  if (geschnitten !== arbeitsPfad) fs.rmSync(arbeitsPfad, { force: true });
  const ohneRand = geschnitten.replace(/\.png$/, "-roh.png");
  fs.copyFileSync(geschnitten, ohneRand);
  const fertig = randFarbe ? bestickern(geschnitten, randFarbe) : geschnitten;
  const m = masse(fertig) || {};
  return { pfad: fertig, ohneRand, breite: m.breite || null, hoehe: m.hoehe || null };
}

/**
 * Erzeugt eine neue thematische Szene mit den festen Herr-Jurist-Charakteren.
 * Ein QA-Fehler bekommt genau einen zweiten Versuch in hoeherer Qualitaet.
 */
export async function charakterMotivZeichnen(ziel, { randFarbe = null, zweck = "bild", slot = null } = {}) {
  if (!charakterBildAktiv() || !ziel) return null;
  const cfg = CONFIG.bilder.charaktere;
  const chars = charaktereFuer(ziel).slice(0, 6);
  if (!chars.length || chars.some((c) => !fs.existsSync(path.join(basis, c.datei)))) return null;
  const prompt = charakterPrompt(ziel, chars);
  const versuche = [
    { quality: cfg.guete, reserve: cfg.reserveUsd },
    { quality: cfg.retryGuete, reserve: cfg.retryReserveUsd },
  ];
  for (let i = 0; i < versuche.length; i++) {
    const v = versuche[i];
    try {
      const daten = await bildAufruf({
        zweck,
        modell: cfg.modell,
        optional: true,
        preisUsd: v.reserve,
        zeitlimitMs: cfg.zeitlimitMs,
        slot: slot || ziel?.slug || ziel?.themaId || ziel?.titel || "charakter",
        senden: () => editAufruf({
          chars, prompt, quality: v.quality, size: cfg.groesse,
          key: CONFIG.bilder.ki.key, modell: cfg.modell, zeitlimitMs: cfg.zeitlimitMs,
        }),
        kostenAusAntwort: bildKostenUsd,
      });
      const roh = dateiAusAntwort(daten);
      if (!roh) continue;
      const fertig = qa(roh, cfg.randAktiv ? randFarbe : null);
      if (!fertig) {
        console.warn(`  ! Charakterbild QA fehlgeschlagen (${chars.map((c) => c.name).join(" + ")}, Versuch ${i + 1})`);
        continue;
      }
      const kosten = bildKostenUsd(daten);
      console.log(`  → Charakterbild: ${chars.map((c) => c.name).join(" + ")} · ${v.quality}${kosten != null ? ` · ${kosten.toFixed(4)} $` : ""}`);
      return { ...fertig, charaktere: chars.map((c) => c.name), prompt, kostenUsd: kosten };
    } catch (e) {
      console.warn(`  ! Charakterbild Versuch ${i + 1} fehlgeschlagen: ${e.message.slice(0, 180)}`);
      /* Ein 4xx-Eingabefehler wird durch hoehere Qualitaet nicht besser.
         Nur ein inhaltlich/visuell misslungenes, aber technisch erzeugtes Bild
         bekommt den teureren High-Retry. */
      if (Number(e?.status) >= 400 && Number(e?.status) < 500 && Number(e?.status) !== 429) break;
    }
  }
  return null;
}
