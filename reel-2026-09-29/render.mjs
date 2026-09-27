import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root = path.resolve('reel-2026-09-29');
const audio = path.join(root, 'audio');
const out = path.join(root, 'out');
fs.mkdirSync(audio, { recursive: true });
fs.mkdirSync(out, { recursive: true });

// One case: Rex's single signature is rejected, the contractual and statutory
// representation rule explains why, Mara co-signs, then the exam takeaway.
const lines = [
  'Rex unterschreibt allein.',
  'Vertrag geschlossen? Stopp!',
  'Er und Mara betreiben die Sternwerkstatt-GbR.',
  'Der Gesellschaftsvertrag regelt die Vertretung nicht; eine Ermächtigung fehlt.',
  'Dann gilt Paragraf siebenhundertzwanzig BGB: Beide vertreten gemeinsam.',
  'Rex allein bindet die GbR zunächst nicht.',
  'Mara zeichnet mit: Das Vertragstor öffnet sich.',
  'Merke: Gesellschaftsvertrag, Vertretungsordnung, Vertreterhandeln.'
];
const script = lines.join(' ');
const voice = process.env.ELEVENLABS_VOICE_ID || 'PhufIH7nYh2Up1uej6aY';
const model = process.env.ELEVENLABS_MODEL || 'eleven_multilingual_v2';
const key = process.env.ELEVENLABS_API_KEY;
const voicePath = path.join(audio, 'sprecher.mp3');
const alignmentPath = path.join(audio, 'alignment.json');
const run = (cmd, args) => {
  const r = spawnSync(cmd, args, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
  if (r.status !== 0) throw new Error(`${cmd} ${args.join(' ')}: ${r.stderr.slice(-4000)}`);
  return r.stdout.trim();
};
const duration = p => Number(run('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'default=nw=1:nk=1', p]));
const ms = t => Math.max(0, Math.round(t * 1000));
const fps = 30, lead = .42;

if (!fs.existsSync(voicePath) || !fs.existsSync(alignmentPath)) {
  if (!key) throw new Error('ELEVENLABS_API_KEY fehlt; die freigegebene Stimme wird benötigt.');
  const r = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${encodeURIComponent(voice)}/with-timestamps?output_format=mp3_44100_128`, {
    method: 'POST',
    headers: { 'xi-api-key': key, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: script, model_id: model, language_code: 'de',
      voice_settings: { stability: .42, similarity_boost: .8, style: .36, use_speaker_boost: true, speed: 1.06 } })
  });
  if (!r.ok) throw new Error(`ElevenLabs TTS ${r.status}: ${(await r.text()).slice(0, 400)}`);
  const data = await r.json();
  fs.writeFileSync(voicePath, Buffer.from(data.audio_base64, 'base64'));
  fs.writeFileSync(alignmentPath, JSON.stringify({ script, alignment: data.alignment, normalized_alignment: data.normalized_alignment }, null, 2));
}

const voiceDuration = duration(voicePath);
const raw = JSON.parse(fs.readFileSync(alignmentPath));
if (raw.script !== script) throw new Error('Gespeicherte ElevenLabs-Stimme gehört zu einem anderen Sprechertext.');
const choices = [raw.alignment, raw.normalized_alignment].filter(Boolean);
const selected = choices.find(a => a.characters?.join('') === script) || choices.find(a => a.character_end_times_seconds?.length === script.length);
if (!selected) throw new Error('Kein zeichengetreues ElevenLabs-Alignment für Einzelwort-Captions verfügbar.');
const starts = selected.character_start_times_seconds;
const ends = selected.character_end_times_seconds;
const charStart = i => Math.max(0, starts[i] ?? voiceDuration * i / script.length) + lead;
const charEnd = i => Math.max(0, ends[i] ?? voiceDuration * (i + 1) / script.length) + lead;
const boundaries = [0];
let cursor = 0;
for (const line of lines) {
  cursor += line.length;
  boundaries.push(charEnd(cursor - 1) + .04);
  cursor++;
}
const finalDuration = Math.max(voiceDuration + lead + .50, boundaries.at(-1) + .35);
boundaries[boundaries.length - 1] = finalDuration;
if (boundaries.some((x, i) => i && x <= boundaries[i - 1])) throw new Error('Satzgrenzen des Sprecher-Alignments ungültig.');

const stamp = t => {
  const cs = Math.round(t * 100);
  return `${Math.floor(cs / 360000)}:${String(Math.floor(cs / 6000) % 60).padStart(2, '0')}:${String(Math.floor(cs / 100) % 60).padStart(2, '0')}.${String(cs % 100).padStart(2, '0')}`;
};
const header = `[Script Info]\nTitle: Herr Jurist 29.09. – Sprecher als Einzelwort-Captions\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\nScaledBorderAndShadow: yes\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Word,Nimbus Sans,72,&H00FAFAFA&,&H00FAFAFA&,&H00191919&,&H90000000&,-1,0,0,0,100,100,0,0,1,2.5,2,2,110,170,280,1\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n`;
let ass = header;
let cueCount = 0;
const spokenWords = [...script.matchAll(/\S+/g)];
for (let i = 0; i < spokenWords.length; i++) {
  const m = spokenWords[i];
  const legalCitation = m[0] === 'Paragraf' && spokenWords[i + 1]?.[0] === 'siebenhundertzwanzig';
  // The spoken legal reference is one semantic caption: its printed citation.
  const word = legalCitation ? '§ 720' : m[0];
  const from = m.index;
  const last = legalCitation ? spokenWords[++i] : m;
  const to = last.index + last[0].length - 1;
  let start = charStart(from), end = charEnd(to);
  if (end < start + .10) end = start + .10;
  // A pause between words stays empty; the citation alone spans two spoken words.
  const size = word.length > 28 ? 55 : word.length > 21 ? 64 : 72;
  const display = word.replaceAll('{', '').replaceAll('}', '');
  ass += `Dialogue: 0,${stamp(start)},${stamp(end)},Word,,0,0,0,,{\\fs${size}\\fad(35,40)\\fscx106\\fscy106\\t(0,110,\\fscx100\\fscy100)}${display}\n`;
  cueCount++;
}
const assPath = path.join(out, 'untertitel-einzelwort.ass');
fs.writeFileSync(assPath, ass);

// Cuts occur on the words and physical actions, never as a continuous zoom.
const openIndex = script.indexOf('Das Vertragstor');
const opening = charStart(openIndex);
const b = boundaries;
const beats = [
  { at: 0, until: b[1], image: '01-signing.jpg', note: 'pen about to touch' },
  { at: b[1], until: b[1] + .067, image: '02-blocked.jpg', punch: 1.11, event: 'denial' },
  { at: b[1] + .067, until: b[2], image: '02-blocked.jpg', note: 'rejection reaction' },
  { at: b[2], until: b[3], image: '03-partners.jpg', note: 'two partners' },
  { at: b[3], until: b[4], image: '04-contract.jpg', note: 'agreement checked' },
  { at: b[4], until: b[5], image: '05-law.jpg', event: 'law', note: 'integrated § 720' },
  { at: b[5], until: b[6], image: '02-blocked.jpg', punch: 1.07, note: 'single signature revisited' },
  { at: b[6], until: opening, image: '06-cosign.jpg', note: 'Mara adds signature' },
  { at: opening, until: opening + .067, image: '07-unlocked.jpg', punch: 1.08, event: 'open' },
  { at: opening + .067, until: b[7], image: '07-unlocked.jpg', note: 'gate opens' },
  { at: b[7], until: b[8], image: '08-merke.jpg', note: 'in-world takeaway' }
];
if (beats.some(x => x.until <= x.at + .04)) throw new Error(`Zu kurzer Bildbeat: ${JSON.stringify(beats)}`);
for (let i = 0; i < beats.length; i++) {
  const x = beats[i];
  const source = path.join(root, 'shots', x.image);
  if (!fs.existsSync(source)) throw new Error(`Bild fehlt: ${source}`);
  const target = path.join(out, `beat-${String(i + 1).padStart(2, '0')}.mp4`);
  const n = Math.max(2, Math.round(x.until * fps) - Math.round(x.at * fps));
  const zoom = x.punch || 1;
  const width = Math.round(1080 * zoom / 2) * 2, height = Math.round(1920 * zoom / 2) * 2;
  const vf = `scale=${width}:${height}:force_original_aspect_ratio=increase,crop=1080:1920:(iw-1080)/2:(ih-1920)/2,format=yuv420p`;
  run('ffmpeg', ['-y', '-loglevel', 'error', '-loop', '1', '-framerate', String(fps), '-i', source,
    '-vf', vf, '-frames:v', String(n), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-an', target]);
  x.frames = n; x.actualAt = i ? beats[i - 1].actualAt + beats[i - 1].frames / fps : 0;
  x.output = target;
}
const concat = path.join(out, 'concat.txt');
fs.writeFileSync(concat, beats.map(x => `file '${x.output}'`).join('\n') + '\n');
const silent = path.join(out, 'silent.mp4');
run('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', concat, '-c', 'copy', silent]);

const effects = [
  { name: 'deny', event: 'denial', offset: 0, seconds: 1.1, volume: .36,
    prompt: 'One crisp futuristic document scanner REJECTION: sudden electrical BZZT with sharp metallic click, short blue energy crackle, no scream, no words, no music.' },
  { name: 'law', event: 'law', offset: .08, seconds: 1.3, volume: .17,
    prompt: 'Short elegant futuristic holographic legal panel projection swell and subtle rising glassy chime, precise and restrained, no words, no music.' },
  { name: 'open', event: 'open', offset: 0, seconds: 1.7, volume: .30,
    prompt: 'Decisive sci-fi contract approval chime followed immediately by a heavy high-tech door unlocking and opening with bright metallic servo whoosh, satisfying clean attack, no speech, no music.' }
];
for (const e of effects) {
  e.path = path.join(audio, `${e.name}.mp3`);
  if (fs.existsSync(e.path)) continue;
  if (!key) throw new Error(`ElevenLabs SFX ${e.name} fehlt.`);
  const r = await fetch('https://api.elevenlabs.io/v1/sound-generation', { method: 'POST',
    headers: { 'xi-api-key': key, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: e.prompt, duration_seconds: e.seconds, prompt_influence: .75, model_id: 'eleven_text_to_sound_v2' }) });
  if (!r.ok) throw new Error(`ElevenLabs SFX ${e.name} ${r.status}: ${(await r.text()).slice(0, 400)}`);
  fs.writeFileSync(e.path, Buffer.from(await r.arrayBuffer()));
}

const filters = [`[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,adelay=${ms(lead)}:all=1,volume=.84[v]`];
effects.forEach((e, i) => {
  e.actualAt = beats.find(x => x.event === e.event).actualAt + e.offset;
  filters.push(`[${i + 2}:a]highpass=f=100,volume=${e.volume},adelay=${ms(e.actualAt)}:all=1[s${i}]`);
});
filters.push(`[v]${effects.map((_, i) => `[s${i}]`).join('')}amix=inputs=${effects.length + 1}:duration=longest:normalize=0,alimiter=limit=0.90,apad[a]`);
const dest = path.join(out, 'herrjurist-2026-09-29-gbr-prueffassung.mp4');
run('ffmpeg', ['-y', '-loglevel', 'error', '-i', silent, '-i', voicePath, ...effects.flatMap(e => ['-i', e.path]),
  '-filter_complex', filters.join(';'), '-map', '0:v:0', '-map', '[a]', '-vf', `ass=${assPath}`,
  '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p',
  '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-t', String(finalDuration), '-movflags', '+faststart', dest]);
if (fs.statSync(dest).size < 1_000_000 || duration(dest) < finalDuration - .2) throw new Error('MP4 unvollständig.');
const cover = path.join(out, 'cover.jpg');
run('ffmpeg', ['-y', '-loglevel', 'error', '-ss', '0.8', '-i', dest, '-frames:v', '1', '-q:v', '3', cover]);
fs.writeFileSync(path.join(out, 'timing.json'), JSON.stringify({ script, voice, model, lead, voiceDuration,
  finalDuration, captionCues: cueCount, boundaries, effects: effects.map(({ path: _, ...e }) => e),
  beats: beats.map(({ output: _, ...x }) => x) }, null, 2));
console.log(`${dest} ${duration(dest).toFixed(2)}s ${cueCount} narrator word captions`);
