import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root = path.resolve('reel-2026-09-30');
const audio = path.join(root, 'audio');
const out = path.join(root, 'out');
const framesDir = path.join(out, 'frames');
for (const dir of [audio, out, framesDir]) fs.mkdirSync(dir, { recursive: true });

// One causal story. The signature is shown first, then the earlier prohibited
// interrogation explains why that signature cannot save this statement.
const lines = [
  'Zylla unterschreibt: Meine Aussage dürft ihr nutzen. Klingt wirksam?',
  'Zurück in die Vernehmung.',
  'Brakk hält sie die ganze Nacht wach, bis sie erschöpft redet.',
  'Zylla ist längst am Ende, doch er fragt weiter.',
  'Ihre Aussage landet trotzdem im Protokoll.',
  'Doch Paragraf einhundertsechsunddreißig A der Strafprozessordnung verbietet solche Ermüdung.',
  'Absatz drei: Auch Zyllas spätere Zustimmung macht diese Aussage nicht verwertbar.',
  'Eine Unterschrift heilt keine verbotene Vernehmungsmethode.'
];
const script = lines.join(' ');
const voice = process.env.ELEVENLABS_VOICE_ID || 'PhufIH7nYh2Up1uej6aY';
const model = process.env.ELEVENLABS_MODEL || 'eleven_multilingual_v2';
const key = process.env.ELEVENLABS_API_KEY;
const voicePath = path.join(audio, 'sprecher.mp3');
const alignmentPath = path.join(audio, 'alignment.json');
const fps = 30;
const lead = .40;
const run = (cmd, args) => {
  const r = spawnSync(cmd, args, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
  if (r.status !== 0) throw new Error(`${cmd} failed: ${r.stderr.slice(-5000)}`);
  return r.stdout.trim();
};
const mediaDuration = file => Number(run('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'default=nw=1:nk=1', file]));
const ms = t => Math.max(0, Math.round(t * 1000));
if (!fs.existsSync(voicePath) || !fs.existsSync(alignmentPath)) {
  if (!key) throw new Error('ELEVENLABS_API_KEY fehlt für neue Sprecheraufnahme.');
  const r = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${encodeURIComponent(voice)}/with-timestamps?output_format=mp3_44100_128`, {
    method: 'POST', headers: { 'xi-api-key': key, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: script, model_id: model, language_code: 'de',
      voice_settings: { stability: .42, similarity_boost: .8, style: .36, use_speaker_boost: true, speed: 1.06 } })
  });
  if (!r.ok) throw new Error(`ElevenLabs narration ${r.status}: ${(await r.text()).slice(0, 400)}`);
  const data = await r.json();
  fs.writeFileSync(voicePath, Buffer.from(data.audio_base64, 'base64'));
  fs.writeFileSync(alignmentPath, JSON.stringify({ script, alignment: data.alignment, normalized_alignment: data.normalized_alignment }, null, 2));
}
const voiceDuration = mediaDuration(voicePath);
const raw = JSON.parse(fs.readFileSync(alignmentPath));
if (raw.script !== script) throw new Error('Alignment und aktueller Sprechertext unterscheiden sich.');
const a = [raw.alignment, raw.normalized_alignment].filter(Boolean).find(x => x.characters?.join('') === script);
if (!a) throw new Error('Kein zeichengetreues ElevenLabs-Alignment.');
const charStart = i => (a.character_start_times_seconds[i] ?? voiceDuration * i / script.length) + lead;
const charEnd = i => (a.character_end_times_seconds[i] ?? voiceDuration * (i + 1) / script.length) + lead;
const boundaries = [0];
let pos = 0;
for (const line of lines) { pos += line.length; boundaries.push(charEnd(pos - 1) + .03); pos++; }
const finalDuration = Math.max(voiceDuration + lead + .45, boundaries.at(-1) + .25);
boundaries[boundaries.length - 1] = finalDuration;
if (boundaries.some((t, i) => i && t <= boundaries[i - 1])) throw new Error('Ungültiges Satz-Timing.');

const stamp = t => {
  const cs = Math.round(t * 100);
  return `${Math.floor(cs / 360000)}:${String(Math.floor(cs / 6000) % 60).padStart(2, '0')}:${String(Math.floor(cs / 100) % 60).padStart(2, '0')}.${String(cs % 100).padStart(2, '0')}`;
};
let ass = `[Script Info]\nTitle: Herr Jurist 30.09 – § 136a StPO\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\nScaledBorderAndShadow: yes\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Word,Nimbus Sans,72,&H00FAFAFA&,&H00FAFAFA&,&H00191919&,&H90000000&,-1,0,0,0,100,100,0,0,1,2.5,2,2,110,170,280,1\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n`;
let cues = 0;
const words = [...script.matchAll(/\S+/g)];
for (let i = 0; i < words.length; i++) {
  const m = words[i];
  let to = m.index + m[0].length - 1;
  let display = m[0];
  if (m[0] === 'Paragraf' && words[i + 1]?.[0] === 'einhundertsechsunddreißig' && words[i + 2]?.[0] === 'A') {
    to = words[i + 2].index; display = '§ 136a'; i += 2;
  } else if (m[0] === 'Absatz' && words[i + 1]?.[0] === 'drei:') {
    to = words[i + 1].index + words[i + 1][0].length - 1; display = 'Abs. 3:'; i++;
  } else if (m[0] === 'Strafprozessordnung') display = 'StPO';
  let start = charStart(m.index), end = charEnd(to);
  if (end < start + .10) end = start + .10;
  const size = display.length > 28 ? 55 : display.length > 21 ? 64 : 72;
  display = display.replaceAll('{', '').replaceAll('}', '');
  ass += `Dialogue: 0,${stamp(start)},${stamp(end)},Word,,0,0,0,,{\\fs${size}\\fad(35,40)\\fscx106\\fscy106\\t(0,110,\\fscx100\\fscy100)}${display}\n`;
  cues++;
}
fs.writeFileSync(path.join(out, 'untertitel-einzelwort.ass'), ass);

// The sheets are solely generation layouts. Each cell becomes a separate
// full-screen image in strict row-major story order; no grid is in the reel.
const sheets = [
  ['01-hook.png', 2], ['02-rejection.png', 2], ['03-rewind.png', 2],
  ['04-interrogation.png', 2], ['05-overnight.png', 3],
  ['06-breaking-point.png', 3], ['07-recording.png', 3],
  ['08-law.png', 3], ['09-barrier.png', 3], ['10-pointe.png', 3]
];
const groups = [
  [0, 1], [2], [3, 4], [5], [6], [7], [8], [9]
];
const lawTop = path.join(out, 'norm-top.txt');
const lawBottom = path.join(out, 'norm-bottom.txt');
fs.writeFileSync(lawTop, '§ 136a');
fs.writeFileSync(lawBottom, 'Abs. 3 StPO');
const framesBySheet = [];
for (let si = 0; si < sheets.length; si++) {
  const [name, cols] = sheets[si];
  const source = path.join(root, 'sheets', name);
  if (!fs.existsSync(source)) throw new Error(`Storyboard fehlt: ${name}`);
  const dims = run('ffprobe', ['-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=p=0:s=x', source]).split('x').map(Number);
  const [width, height] = dims; const rows = cols;
  const cellW = Math.floor(width / cols), cellH = Math.floor(height / rows);
  const cropH = Math.min(cellH - 16, Math.floor((cellW - 16) * 16 / 9));
  const cropW = Math.floor(cropH * 9 / 16);
  if (cropW > cellW - 16) throw new Error(`Panel zu schmal: ${name}`);
  const extracted = [];
  for (let pi = 0; pi < cols * rows; pi++) {
    const x = (pi % cols) * cellW + Math.floor((cellW - cropW) / 2);
    const y = Math.floor(pi / cols) * cellH + Math.floor((cellH - cropH) / 2);
    const dest = path.join(framesDir, `${String(si + 1).padStart(2, '0')}-${String(pi + 1).padStart(2, '0')}.jpg`);
    let vf = `crop=${cropW}:${cropH}:${x}:${y},scale=1080:1920:flags=lanczos,format=yuv420p`;
    if (si === 7 && pi >= 3) {
      const f = 'Nimbus Sans';
      vf += `,drawtext=font='${f}':textfile=${lawTop}:fontsize=76:fontcolor=white:borderw=2:bordercolor=0x512600:x=660-text_w/2:y=392`;
      vf += `,drawtext=font='${f}':textfile=${lawBottom}:fontsize=64:fontcolor=0xffd09a:borderw=2:bordercolor=0x512600:x=660-text_w/2:y=506`;
    }
    run('ffmpeg', ['-y', '-loglevel', 'error', '-i', source, '-vf', vf, '-frames:v', '1', '-q:v', '3', dest]);
    extracted.push(dest);
  }
  framesBySheet.push(extracted);
}
const flat = groups.map(g => g.flatMap(si => framesBySheet[si]));
if (flat.flat().length !== 70) throw new Error('70 Einzelbilder erwartet.');
const intervals = [];
const concat = [];
let frameIndex = 0;
for (let i = 0; i < groups.length; i++) {
  const images = flat[i];
  const start = boundaries[i], end = boundaries[i + 1], each = (end - start) / images.length;
  if (!(each > .18 && each < .9)) throw new Error(`Ungültige Bildphase ${i}: ${each}`);
  intervals.push({ scene: i + 1, from: start, to: end, images: images.length, imagesPerSecond: images.length / (end - start) });
  for (const frame of images) {
    concat.push(`file '${frame}'`, `duration ${each.toFixed(6)}`);
    frameIndex++;
  }
}
concat.push(`file '${flat.at(-1).at(-1)}'`); // concat demuxer retains final duration
const list = path.join(out, 'frames.txt');
fs.writeFileSync(list, concat.join('\n') + '\n');
const silent = path.join(out, 'silent.mp4');
run('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', list,
  '-vf', 'fps=30,format=yuv420p', '-t', String(finalDuration), '-c:v', 'libx264',
  '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-an', silent]);

const effects = [
  { name: 'deny', at: boundaries[0] + (boundaries[1] - boundaries[0]) * .55, volume: .36, seconds: 1.1,
    prompt: 'One crisp futuristic evidence scanner RED REJECTION sound, sharp electrical BZZT and short metallic clack, immediate clean attack, no words, no scream, no music.' },
  { name: 'clock', at: boundaries[2] + .25, volume: .12, seconds: 2.4,
    prompt: 'Tense quiet mechanical wall clock ticking in a late night interrogation room, restrained close dry ticks with slight room tone, no speech, no music.' },
  { name: 'law', at: boundaries[5] + .1, volume: .16, seconds: 1.1,
    prompt: 'A concise futuristic holographic legal panel illuminating, subtle rising glassy electric shimmer, no speech, no music.' },
  { name: 'barrier', at: boundaries[6] + (boundaries[7] - boundaries[6]) * .40, volume: .32, seconds: 1.3,
    prompt: 'Decisive high-tech force barrier locking and stopping an evidence data file, crisp red energy crack and solid metallic impact, no scream, no words, no music.' },
  { name: 'paper', at: boundaries[7] + (boundaries[8] - boundaries[7]) * .50, volume: .22, seconds: 1.1,
    prompt: 'A single paper sheet strikes a futuristic energy barrier and falls onto a steel desk, short bright zap then papery flutter, no voice, no music.' }
];
for (const e of effects) {
  e.path = path.join(audio, `${e.name}.mp3`);
  if (fs.existsSync(e.path)) continue;
  if (!key) throw new Error(`SFX fehlt: ${e.name}`);
  const r = await fetch('https://api.elevenlabs.io/v1/sound-generation', { method: 'POST',
    headers: { 'xi-api-key': key, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: e.prompt, duration_seconds: e.seconds, prompt_influence: .75, model_id: 'eleven_text_to_sound_v2' }) });
  if (!r.ok) throw new Error(`ElevenLabs SFX ${e.name} ${r.status}: ${(await r.text()).slice(0, 400)}`);
  fs.writeFileSync(e.path, Buffer.from(await r.arrayBuffer()));
}
const filters = [`[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,adelay=${ms(lead)}:all=1,volume=.84[v]`];
effects.forEach((e, i) => filters.push(`[${i + 2}:a]highpass=f=100,volume=${e.volume},adelay=${ms(e.at)}:all=1[s${i}]`));
filters.push(`[v]${effects.map((_, i) => `[s${i}]`).join('')}amix=inputs=${effects.length + 1}:duration=longest:normalize=0,alimiter=limit=0.90,apad[a]`);
const dest = path.join(out, 'herrjurist-2026-09-30-136a-prueffassung.mp4');
run('ffmpeg', ['-y', '-loglevel', 'error', '-i', silent, '-i', voicePath, ...effects.flatMap(e => ['-i', e.path]),
  '-filter_complex', filters.join(';'), '-map', '0:v:0', '-map', '[a]', '-vf', `ass=${path.join(out, 'untertitel-einzelwort.ass')}`,
  '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', String(fps),
  '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-t', String(finalDuration), '-movflags', '+faststart', dest]);
if (fs.statSync(dest).size < 1_000_000 || mediaDuration(dest) < finalDuration - .2) throw new Error('MP4 unvollständig.');
const cover = path.join(out, 'cover.jpg');
run('ffmpeg', ['-y', '-loglevel', 'error', '-ss', '0.8', '-i', dest, '-frames:v', '1', '-q:v', '3', cover]);
fs.writeFileSync(path.join(out, 'timing.json'), JSON.stringify({ script, lines, voice, model, fps, lead, voiceDuration,
  finalDuration, captionCues: cues, sourceImages: frameIndex, intervals, boundaries,
  effects: effects.map(({ path: _, ...e }) => e), sheets: sheets.map(([name, cols]) => ({ name, panels: cols * cols })) }, null, 2));
console.log(`${dest} ${mediaDuration(dest).toFixed(2)}s / ${frameIndex} cels / ${fps}fps / ${cues} captions`);
