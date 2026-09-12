/* ==========================================================================
   Weiterverteilen derselben Inhalte auf andere Plattformen – jeder Kanal
   ist aktiv, sobald seine Zugangsdaten als Secrets vorliegen. Fehler auf
   einem Kanal stoppen nie die Instagram-Veröffentlichung.

     threads   Beiträge als Bild-Carousel + Text, Reels als Video
     youtube   Reels als Shorts (OAuth-Refresh-Token, läuft dauerhaft)
     facebook  Beiträge als Foto-Post, Reels als Reel auf der Seite
     tiktok    Reels (Direct Post per Datei-Upload; Refresh-Token 365 Tage, im Tresor)
     linkedin  Beiträge als Text mit Bild (Token 60 Tage – im Bericht gemeldet)
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { CONFIG } from "./config.mjs";
import { tokenVerschluesseln, tokenEntschluesseln, fingerabdruck } from "./instagram.mjs";

const schlafen = (ms) => new Promise((r) => setTimeout(r, ms));

async function json(url, opt = {}) {
  const res = await fetch(url, opt);
  const text = await res.text();
  let body; try { body = JSON.parse(text); } catch { body = { raw: text }; }
  if (!res.ok || body.error) throw new Error(`${res.status} ${JSON.stringify(body.error || body).slice(0, 300)}`);
  return body;
}

/* --- Threads ------------------------------------------------------------- */
async function threads({ art, bildUrls, videoUrl, text }) {
  const { token, nutzerId } = CONFIG.verteilen.threads;
  if (!token || !nutzerId) return null;
  const basis = `https://graph.threads.net/v1.0/${nutzerId}`;
  const q = (p) => new URLSearchParams({ ...p, access_token: token });
  const warten = async (id) => { for (let i = 0; i < 20; i++) { const s = await json(`https://graph.threads.net/v1.0/${id}?${q({ fields: "status" })}`); if (s.status === "FINISHED") return; if (s.status === "ERROR") throw new Error("Threads-Container fehlgeschlagen"); await schlafen(4000); } };
  const kurz = text.slice(0, 480);
  let container;
  if (art === "reel" && videoUrl) {
    container = await json(`${basis}/threads?${q({ media_type: "VIDEO", video_url: videoUrl, text: kurz })}`, { method: "POST" });
  } else if (bildUrls?.length > 1) {
    const kinder = [];
    for (const u of bildUrls.slice(0, 10)) { const c = await json(`${basis}/threads?${q({ media_type: "IMAGE", image_url: u, is_carousel_item: "true" })}`, { method: "POST" }); kinder.push(c.id); }
    for (const id of kinder) await warten(id);
    container = await json(`${basis}/threads?${q({ media_type: "CAROUSEL", children: kinder.join(","), text: kurz })}`, { method: "POST" });
  } else {
    container = await json(`${basis}/threads?${q({ media_type: "IMAGE", image_url: bildUrls[0], text: kurz })}`, { method: "POST" });
  }
  await warten(container.id);
  const pub = await json(`${basis}/threads_publish?${q({ creation_id: container.id })}`, { method: "POST" });
  return pub.id;
}

/* --- YouTube Shorts ------------------------------------------------------ */
async function youtubeToken() {
  const { clientId, clientSecret, refreshToken } = CONFIG.verteilen.youtube;
  const r = await json("https://oauth2.googleapis.com/token", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: new URLSearchParams({ client_id: clientId, client_secret: clientSecret, refresh_token: refreshToken, grant_type: "refresh_token" }) });
  return r.access_token;
}
async function youtube({ art, videoPfad, titel, text, hashtags }) {
  const { clientId, clientSecret, refreshToken } = CONFIG.verteilen.youtube;
  if (art !== "reel" || !clientId || !clientSecret || !refreshToken || !videoPfad) return null;
  const token = await youtubeToken();
  const meta = { snippet: { title: `${titel} #Shorts`.slice(0, 100), description: `${text}\n\n${(hashtags || []).join(" ")}`.slice(0, 4900), categoryId: "27", defaultLanguage: "de" }, status: { privacyStatus: "public", selfDeclaredMadeForKids: false } };
  const init = await fetch("https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status", { method: "POST", headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json", "X-Upload-Content-Type": "video/mp4" }, body: JSON.stringify(meta) });
  if (!init.ok) throw new Error(`YouTube init ${init.status}: ${(await init.text()).slice(0, 200)}`);
  const uploadUrl = init.headers.get("location");
  const daten = fs.readFileSync(videoPfad);
  const up = await fetch(uploadUrl, { method: "PUT", headers: { Authorization: `Bearer ${token}`, "Content-Type": "video/mp4", "Content-Length": String(daten.length) }, body: daten });
  if (!up.ok) throw new Error(`YouTube upload ${up.status}: ${(await up.text()).slice(0, 200)}`);
  return (await up.json()).id;
}

/* --- Facebook-Seite ------------------------------------------------------ */
async function facebook({ art, bildUrls, videoUrl, text }) {
  const { seitenId, token } = CONFIG.verteilen.facebook;
  if (!seitenId || !token) return null;
  const basis = `https://graph.facebook.com/${CONFIG.instagram.version}/${seitenId}`;
  if (art === "reel" && videoUrl) {
    const start = await json(`${basis}/video_reels`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ upload_phase: "start", access_token: token }) });
    await json(`https://rupload.facebook.com/video-reels/${CONFIG.instagram.version}/${start.video_id}`, { method: "POST", headers: { Authorization: `OAuth ${token}`, file_url: videoUrl } });
    for (let i = 0; i < 30; i++) { const s = await json(`https://graph.facebook.com/${CONFIG.instagram.version}/${start.video_id}?fields=status&access_token=${token}`); if (s.status?.video_status === "ready" || s.status?.uploading_phase?.status === "complete") break; await schlafen(5000); }
    const r = await json(`${basis}/video_reels`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ upload_phase: "finish", video_id: start.video_id, video_state: "PUBLISHED", description: text.slice(0, 2000), access_token: token }) });
    return r.post_id || start.video_id;
  }
  /* Mehrere Bilder: erst unveröffentlicht hochladen, dann als ein Post. */
  const ids = [];
  for (const u of (bildUrls || []).slice(0, 10)) { const r = await json(`${basis}/photos`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ url: u, published: false, access_token: token }) }); ids.push(r.id); }
  const r = await json(`${basis}/feed`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ message: text, attached_media: ids.map((id) => ({ media_fbid: id })), access_token: token }) });
  return r.id;
}

/* --- TikTok (Direct Post) ------------------------------------------------
   Drei Dinge, die die naheliegende Fassung im Betrieb scheitern lassen:
   1. PULL_FROM_URL verlangt, dass die Domain des Videos in der TikTok-App als
      eigene verifiziert ist - raw.githubusercontent.com lässt sich nicht
      verifizieren. Deshalb FILE_UPLOAD: Die Datei wird selbst hochgeladen.
   2. Solange TikTok die App nicht geprüft hat, darf sie nur "nur ich"-Videos
      posten. Das wäre ein Konto voller privater Videos. Vor dem Posten wird
      deshalb abgefragt, welche Sichtbarkeit erlaubt ist; ohne "öffentlich"
      wird nicht gepostet, sondern gemeldet.
   3. Der Refresh-Token (365 Tage) kann beim Erneuern wechseln. Der jeweils
      neueste liegt verschlüsselt im Asset-Zweig (state/tiktok.enc), wie der
      Instagram-Token; das Secret ist nur der Startpunkt. */
const TT = "https://open.tiktokapis.com/v2";
const TT_TRESOR = "tiktok.enc";

function ttTresorLesen(stateDir) {
  if (!stateDir) return null;
  try {
    const pfad = path.join(stateDir, TT_TRESOR);
    if (!fs.existsSync(pfad)) return null;
    return tokenEntschluesseln(fs.readFileSync(pfad, "utf8"));
  } catch { return null; }
}
function ttTresorSchreiben(stateDir, daten) {
  if (!stateDir) return;
  try { fs.writeFileSync(path.join(stateDir, TT_TRESOR), tokenVerschluesseln({ ...daten, gespeichert: new Date().toISOString() })); } catch (e) { console.warn(`  ! TikTok-Tresor nicht geschrieben: ${e.message}`); }
}

async function tiktokToken(stateDir) {
  const { clientKey, clientSecret, refreshToken } = CONFIG.verteilen.tiktok;
  /* Neuester Refresh-Token aus dem Tresor - sofern er vom aktuellen Secret
     abstammt. Ein neu gesetztes Secret gewinnt (wie beim Instagram-Token). */
  const tresor = ttTresorLesen(stateDir);
  const herkunft = fingerabdruck(refreshToken);
  const aktuell = tresor?.refreshToken && tresor.herkunft === herkunft ? tresor.refreshToken : refreshToken;
  const r = await json(`${TT}/oauth/token/`, { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: new URLSearchParams({ client_key: clientKey, client_secret: clientSecret, grant_type: "refresh_token", refresh_token: aktuell }) });
  if (r.refresh_token && r.refresh_token !== aktuell) ttTresorSchreiben(stateDir, { refreshToken: r.refresh_token, herkunft });
  return r.access_token;
}

/** Aufteilung eines Uploads in Stücke nach den TikTok-Regeln (5–64 MB je Stück,
    kleinere Dateien in einem Stück, der Rest wandert ins letzte Stück). */
export function tiktokStuecke(groesse, stueck = 32 * 1024 * 1024) {
  const MIN = 5 * 1024 * 1024;
  if (groesse <= Math.max(stueck, MIN) || groesse < MIN) return [{ von: 0, bis: groesse - 1 }];
  const anzahl = Math.floor(groesse / stueck);
  const liste = [];
  for (let i = 0; i < anzahl; i++) liste.push({ von: i * stueck, bis: i === anzahl - 1 ? groesse - 1 : (i + 1) * stueck - 1 });
  return liste;
}

async function tiktok({ art, videoPfad, titel, hashtags }, { stateDir = null, log = console.log } = {}) {
  const { clientKey, clientSecret, refreshToken } = CONFIG.verteilen.tiktok;
  if (art !== "reel" || !clientKey || !clientSecret || !refreshToken || !videoPfad || !fs.existsSync(videoPfad)) return null;
  const token = await tiktokToken(stateDir);
  const kopf = { Authorization: `Bearer ${token}`, "Content-Type": "application/json; charset=UTF-8" };
  /* Was darf dieses Konto? Ohne "öffentlich" (App noch nicht geprüft) wird
     nicht gepostet - ein privates Video nützt niemandem. */
  const info = await json(`${TT}/post/publish/creator_info/query/`, { method: "POST", headers: kopf });
  const erlaubt = info.data?.privacy_level_options || [];
  if (!erlaubt.includes("PUBLIC_TO_EVERYONE")) {
    log(`  ⏸ TikTok: Konto @${info.data?.creator_nickname || "?"} darf nur ${erlaubt.join("/") || "nichts"} posten – die App ist von TikTok noch nicht geprüft. Reel nicht gepostet.`);
    return null;
  }
  const groesse = fs.statSync(videoPfad).size;
  const stuecke = tiktokStuecke(groesse);
  const init = await json(`${TT}/post/publish/video/init/`, { method: "POST", headers: kopf, body: JSON.stringify({
    post_info: { title: `${titel} ${(hashtags || []).slice(0, 5).join(" ")}`.slice(0, 150), privacy_level: "PUBLIC_TO_EVERYONE", disable_duet: false, disable_comment: false, disable_stitch: false, video_cover_timestamp_ms: 1000 },
    source_info: { source: "FILE_UPLOAD", video_size: groesse, chunk_size: stuecke[0].bis - stuecke[0].von + 1, total_chunk_count: stuecke.length },
  }) });
  const { publish_id: publishId, upload_url: uploadUrl } = init.data || {};
  if (!publishId || !uploadUrl) throw new Error(`TikTok init ohne upload_url: ${JSON.stringify(init).slice(0, 200)}`);
  const fd = fs.openSync(videoPfad, "r");
  try {
    for (const st of stuecke) {
      const puffer = Buffer.alloc(st.bis - st.von + 1);
      fs.readSync(fd, puffer, 0, puffer.length, st.von);
      const res = await fetch(uploadUrl, { method: "PUT", headers: { "Content-Type": "video/mp4", "Content-Length": String(puffer.length), "Content-Range": `bytes ${st.von}-${st.bis}/${groesse}` }, body: puffer });
      if (!res.ok && res.status !== 206) throw new Error(`TikTok upload ${res.status}: ${(await res.text()).slice(0, 200)}`);
    }
  } finally { fs.closeSync(fd); }
  /* Kurz nachsehen, ob TikTok das Video angenommen hat; die Verarbeitung
     selbst dauert länger, das Ergebnis steht dann im Konto. */
  for (let i = 0; i < 6; i++) {
    await schlafen(5000);
    const st = await json(`${TT}/post/publish/status/fetch/`, { method: "POST", headers: kopf, body: JSON.stringify({ publish_id: publishId }) });
    const status = st.data?.status;
    if (status === "FAILED") throw new Error(`TikTok: ${st.data?.fail_reason || "fehlgeschlagen"}`);
    if (status === "PUBLISH_COMPLETE" || status === "PROCESSING_UPLOAD" || status === "SEND_TO_USER_INBOX") break;
  }
  return publishId;
}

/* --- LinkedIn (persönliches Profil) ------------------------------------- */
async function linkedin({ art, bildPfade, titel, text }) {
  const { token, personUrn } = CONFIG.verteilen.linkedin;
  if (!token || !personUrn || art === "reel") return null;
  const kopf = { Authorization: `Bearer ${token}`, "Content-Type": "application/json", "X-Restli-Protocol-Version": "2.0.0", "LinkedIn-Version": "202409" };
  let bildUrn = null;
  if (bildPfade?.[0]) {
    const init = await json("https://api.linkedin.com/rest/images?action=initializeUpload", { method: "POST", headers: kopf, body: JSON.stringify({ initializeUploadRequest: { owner: personUrn } }) });
    const up = await fetch(init.value.uploadUrl, { method: "PUT", headers: { Authorization: `Bearer ${token}` }, body: fs.readFileSync(bildPfade[0]) });
    if (!up.ok) throw new Error(`LinkedIn upload ${up.status}`);
    bildUrn = init.value.image;
  }
  const body = { author: personUrn, commentary: `${titel}\n\n${text}`.slice(0, 2900), visibility: "PUBLIC", distribution: { feedDistribution: "MAIN_FEED", targetEntities: [], thirdPartyDistributionChannels: [] }, lifecycleState: "PUBLISHED", isReshareDisabledByAuthor: false, ...(bildUrn ? { content: { media: { id: bildUrn, title: titel.slice(0, 200) } } } : {}) };
  const res = await fetch("https://api.linkedin.com/rest/posts", { method: "POST", headers: kopf, body: JSON.stringify(body) });
  if (!res.ok) throw new Error(`LinkedIn ${res.status}: ${(await res.text()).slice(0, 200)}`);
  return res.headers.get("x-restli-id");
}

export const KANAELE = { threads, youtube, facebook, tiktok, linkedin };

/**
 * Verteilt einen veröffentlichten Inhalt auf alle konfigurierten Kanäle.
 * @param {{art:"beitrag"|"reel", bildUrls?, bildPfade?, videoUrl?, videoPfad?, titel, text, hashtags}} inhalt
 * @returns {Object<string, {id?:string, fehler?:string}>}
 */
export async function verteilen(inhalt, { log = console.log, trockenlauf = false, stateDir = null } = {}) {
  const ergebnis = {};
  for (const [name, fn] of Object.entries(KANAELE)) {
    try {
      if (trockenlauf) { const k = CONFIG.verteilen[name]; if (Object.values(k).some(Boolean)) ergebnis[name] = { id: "trocken" }; continue; }
      const id = await fn(inhalt, { stateDir, log });
      if (id) { ergebnis[name] = { id }; log(`  ↗ ${name}: ${id}`); }
    } catch (e) {
      ergebnis[name] = { fehler: e.message };
      console.error(`  ✗ ${name}: ${e.message}`);
    }
  }
  return ergebnis;
}
