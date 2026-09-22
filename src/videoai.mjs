import fs from "node:fs/promises";
import path from "node:path";

const MODELL = "fal-ai/ltx-2.3/image-to-video/fast";
const QUEUE_URL = `https://queue.fal.run/${MODELL}`;
const ERLAUBTE_DAUER = new Set([6, 8, 10]);
const ERLAUBTE_AUFLOESUNG = new Set(["1080p", "1440p", "2160p"]);
const ERLAUBTE_FPS = new Set([24, 25, 48, 50]);

const warten = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function mimeFuerDatei(datei) {
  const name = String(datei).replace(/\.b64$/i, "").toLowerCase();
  if (name.endsWith(".png")) return "image/png";
  if (name.endsWith(".webp")) return "image/webp";
  if (name.endsWith(".gif")) return "image/gif";
  if (name.endsWith(".avif")) return "image/avif";
  if (name.endsWith(".heic")) return "image/heic";
  if (name.endsWith(".heif")) return "image/heif";
  if (name.endsWith(".jpg") || name.endsWith(".jpeg")) return "image/jpeg";
  throw new Error(`Nicht unterstuetztes Bildformat: ${datei}`);
}

async function bildAlsDataUri(datei) {
  const mime = mimeFuerDatei(datei);
  if (/\.b64$/i.test(datei)) {
    const basis64 = (await fs.readFile(datei, "utf8")).replace(/\s+/g, "");
    if (!basis64) throw new Error(`Leere Base64-Datei: ${datei}`);
    return `data:${mime};base64,${basis64}`;
  }
  const puffer = await fs.readFile(datei);
  if (!puffer.length) throw new Error(`Leere Bilddatei: ${datei}`);
  return `data:${mime};base64,${puffer.toString("base64")}`;
}

async function falJson(url, { methode = "GET", body, signal } = {}) {
  const schluessel = String(process.env.FAL_KEY || "").trim();
  if (!schluessel) {
    throw new Error("FAL_KEY fehlt. Lege ihn als GitHub Actions Secret bzw. Umgebungsvariable an.");
  }

  const antwort = await fetch(url, {
    method: methode,
    headers: {
      Authorization: `Key ${schluessel}`,
      Accept: "application/json",
      ...(body === undefined ? {} : { "Content-Type": "application/json" }),
    },
    ...(body === undefined ? {} : { body: JSON.stringify(body) }),
    signal,
  });

  const text = await antwort.text();
  let daten = null;
  if (text) {
    try {
      daten = JSON.parse(text);
    } catch {
      daten = { raw: text.slice(0, 1200) };
    }
  }

  if (!antwort.ok) {
    const detail = daten?.detail || daten?.error || daten?.message || daten?.raw || `HTTP ${antwort.status}`;
    throw new Error(`fal.ai: ${antwort.status} ${String(detail).slice(0, 1200)}`);
  }
  return daten || {};
}

function statusName(daten) {
  return String(daten?.status || daten?.state || "").toUpperCase();
}

function fehlerAusStatus(daten) {
  return daten?.error || daten?.detail || daten?.message || daten?.logs?.at?.(-1)?.message || null;
}

/**
 * Reiner Testpfad fuer fal.ai / LTX-2.3 Fast.
 *
 * Wichtig: Diese Funktion ist absichtlich noch NICHT in den produktiven
 * Reel-Lauf eingebaut. Sie erzeugt genau einen Clip und hat keinen Retry,
 * der versehentlich einen zweiten kostenpflichtigen Auftrag ausloesen koennte.
 */
export async function videoAusBild({
  bild,
  imageUrl,
  prompt,
  ausgabe,
  dauer = 6,
  aufloesung = "1080p",
  seitenverhaeltnis = "9:16",
  fps = 25,
  timeoutMs = 15 * 60 * 1000,
  pollMs = 5000,
} = {}) {
  if (!prompt || !String(prompt).trim()) throw new Error("Ein Bewegungs-Prompt ist Pflicht.");
  if (!ausgabe) throw new Error("Ein Ausgabepfad fuer das MP4 ist Pflicht.");
  if (!imageUrl && !bild) throw new Error("Uebergib imageUrl oder einen lokalen Bildpfad.");
  if (!ERLAUBTE_DAUER.has(Number(dauer))) throw new Error("Testdauer muss 6, 8 oder 10 Sekunden sein.");
  if (!ERLAUBTE_AUFLOESUNG.has(aufloesung)) throw new Error("Unbekannte Aufloesung.");
  if (!ERLAUBTE_FPS.has(Number(fps))) throw new Error("FPS muss 24, 25, 48 oder 50 sein.");
  if (!["auto", "9:16", "16:9"].includes(seitenverhaeltnis)) throw new Error("Unbekanntes Seitenverhaeltnis.");

  const quelle = imageUrl || await bildAlsDataUri(bild);
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(new Error("fal.ai-Test hat das Zeitlimit ueberschritten.")), timeoutMs);

  try {
    const start = await falJson(QUEUE_URL, {
      methode: "POST",
      body: {
        image_url: quelle,
        prompt: String(prompt).trim(),
        duration: Number(dauer),
        resolution: aufloesung,
        aspect_ratio: seitenverhaeltnis,
        fps: Number(fps),
        generate_audio: false,
      },
      signal: controller.signal,
    });

    const requestId = start.request_id || start.requestId;
    if (!requestId) throw new Error(`fal.ai lieferte keine request_id: ${JSON.stringify(start).slice(0, 1200)}`);

    const statusUrl = start.status_url || `${QUEUE_URL}/requests/${encodeURIComponent(requestId)}/status`;
    const responseUrl = start.response_url || `${QUEUE_URL}/requests/${encodeURIComponent(requestId)}`;

    let letzterStatus = "";
    while (true) {
      const status = await falJson(statusUrl, { signal: controller.signal });
      const name = statusName(status);

      if (name && name !== letzterStatus) {
        console.log(`fal.ai: ${name}`);
        letzterStatus = name;
      }

      if (["COMPLETED", "SUCCEEDED", "SUCCESS"].includes(name)) break;
      if (["FAILED", "ERROR", "CANCELLED", "CANCELED"].includes(name)) {
        throw new Error(`fal.ai-Auftrag fehlgeschlagen: ${fehlerAusStatus(status) || name}`);
      }
      await warten(pollMs);
    }

    const ergebnis = await falJson(responseUrl, { signal: controller.signal });
    const daten = ergebnis?.data || ergebnis;
    const video = daten?.video;
    if (!video?.url) {
      throw new Error(`fal.ai lieferte kein Video: ${JSON.stringify(ergebnis).slice(0, 1600)}`);
    }

    const download = await fetch(video.url, { signal: controller.signal });
    if (!download.ok) throw new Error(`Video-Download fehlgeschlagen: HTTP ${download.status}`);
    const puffer = Buffer.from(await download.arrayBuffer());

    await fs.mkdir(path.dirname(ausgabe), { recursive: true });
    await fs.writeFile(ausgabe, puffer);

    return {
      requestId,
      modell: MODELL,
      videoUrl: video.url,
      ausgabe,
      dauer: Number(dauer),
      aufloesung,
      seitenverhaeltnis,
      fps: Number(fps),
      bytes: puffer.length,
    };
  } finally {
    clearTimeout(timer);
  }
}

export const FAL_VIDEO_TEST_MODELL = MODELL;
