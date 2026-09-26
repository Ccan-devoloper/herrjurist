import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const dir = path.resolve('reel-test-2026-09-27');
const out = path.join(dir, 'out-v3');
fs.mkdirSync(out, { recursive: true });
const lines = [
  'Rex schlägt Mara mit einem Thermobecher.',
  'Gefährliche Körperverletzung? Ein Becher ist doch keine Waffe.',
  'Aber bei Paragraf zweihundertvierundzwanzig zählt der konkrete Einsatz.',
  'Harter Becher, voller Schwung, Treffer am Kopf: Kann das erhebliche Verletzungen verursachen?',
  'Dann kann er ein gefährliches Werkzeug sein. Merke: Beschaffenheit und Verwendung prüfen.'
];
const script = lines.join(' ');
const key = process.env.ELEVENLABS_API_KEY;
const voice = process.env.ELEVENLABS_VOICE_ID || 'PhufIH7nYh2Up1uej6aY';
const model = process.env.ELEVENLABS_MODEL || 'eleven_multilingual_v2';
function run(command, args) {
  const result = spawnSync(command, args, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
  if (result.status !== 0) throw new Error(`${command}: ${result.stderr.slice(-2000)}`);
  return result.stdout.trim();
}
function duration(file) { return Number(run('ffprobe', ['-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',file])); }

let voicePath = process.env.REEL_VOICE_PATH;
let alignment;
if (!voicePath) {
  if (!key) throw new Error('ELEVENLABS_API_KEY fehlt. Für lokalen Schnitt REEL_VOICE_PATH setzen.');
  const response = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${encodeURIComponent(voice)}/with-timestamps?output_format=mp3_44100_128`, {
    method: 'POST', headers: { 'xi-api-key': key, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: script, model_id: model, language_code: 'de', voice_settings: { stability: 0.42, similarity_boost: 0.8, style: 0.36, use_speaker_boost: true, speed: 1.06 } })
  });
  if (!response.ok) throw new Error(`ElevenLabs TTS ${response.status}: ${(await response.text()).slice(0, 200)}`);
  const spoken = await response.json();
  voicePath = path.join(out, 'sprecher-elevenlabs.mp3');
  fs.writeFileSync(voicePath, Buffer.from(spoken.audio_base64, 'base64'));
  alignment = spoken.alignment?.character_end_times_seconds || spoken.normalized_alignment?.character_end_times_seconds;
}
const voiceDuration = duration(voicePath);
let char = 0;
const boundaries = lines.map((line, i) => {
  char += line.length;
  const seconds = alignment?.[char - 1] ?? voiceDuration * char / script.length;
  if (i < lines.length - 1) char++;
  return Math.min(voiceDuration, seconds);
});
// If no word alignment is available, match the timing of the approved clean voice.
const base = alignment ? [0, ...boundaries.slice(0,4), voiceDuration + 0.6] :
  [0,2.3,6.2,10.5,16.6,voiceDuration + 0.6].map(x => x * voiceDuration / 22.296);
base[5] = voiceDuration + 0.6;
const b = base;
const beats = [
  {at:0, until:Math.min(.62,b[1]*.36), image:'shot-01.jpg', label:'Ein Becher?'},
  {at:Math.min(.62,b[1]*.36), until:b[1], image:'shot-01.jpg', punch:1.18},
  {at:b[1], until:b[1]+(b[2]-b[1])*.59, image:'shot-06-aftermath.jpg'},
  {at:b[1]+(b[2]-b[1])*.59, until:b[2], image:'shot-03.jpg'},
  {at:b[2], until:b[2]+(b[3]-b[2])*.53, image:'shot-09-rule.jpg'},
  {at:b[2]+(b[3]-b[2])*.53, until:b[3], image:'shot-07-mug-scan.jpg'},
  {at:b[3], until:b[3]+(b[4]-b[3])*.33, image:'shot-04.jpg'},
  {at:b[3]+(b[4]-b[3])*.33, until:b[3]+(b[4]-b[3])*.70, image:'shot-08-impact-close.jpg'},
  {at:b[3]+(b[4]-b[3])*.70, until:b[4], image:'shot-06-aftermath.jpg'},
  {at:b[4], until:b[4]+(b[5]-b[4])*.46, image:'shot-05.jpg', label:'§ 224 I Nr. 2'},
  {at:b[4]+(b[5]-b[4])*.46, until:b[5], image:'shot-05.jpg', punch:1.14, label:'§ 224 I Nr. 2'}
];
const font = path.resolve('fonts/Inter.ttf');
const fps = 30;
for (let i = 0; i < beats.length; i++) {
  const beat = beats[i];
  const input = path.join(dir, 'shots', beat.image);
  const output = path.join(out, `scene-${String(i+1).padStart(2,'0')}.mp4`);
  const punch = beat.punch || 1;
  const w = Math.round(1080 * punch / 2) * 2;
  const h = Math.round(1920 * punch / 2) * 2;
  // These dimensions and crop offsets are fixed for every frame: no zoompan or per-frame motion.
  let filter = `scale=${w}:${h}:force_original_aspect_ratio=increase,crop=1080:1920:(iw-1080)/2:(ih-1920)/2,format=yuv420p`;
  if (beat.label) filter += `,drawtext=fontfile=${font}:text='${beat.label}':fontsize=${beat.label.startsWith('§')?66:76}:fontcolor=white:borderw=4:bordercolor=black:box=1:boxcolor=black@0.58:boxborderw=20:x=(w-text_w)/2:y=285`;
  const args = ['-y','-loglevel','error','-loop','1','-framerate',String(fps),'-i',input,'-vf',filter,'-frames:v',String(Math.round((beat.until-beat.at)*fps)),'-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-an',output];
  run('ffmpeg', args);
  beat.encodeArgs = args;
  beat.output = output;
}
// Verify every file after the whole batch, since a truncated MP4 would stop concat early.
for (const beat of beats) {
  let ok = false;
  for (let attempt = 0; attempt < 3 && !ok; attempt++) {
    try { ok = fs.statSync(beat.output).size > 1000 && duration(beat.output) > 0.1; } catch {}
    if (!ok) run('ffmpeg', beat.encodeArgs);
  }
  if (!ok) throw new Error(`Leeres Segment: ${beat.output}`);
}
const concat = path.join(out,'concat.txt');
fs.writeFileSync(concat, beats.map(x => `file '${x.output}'`).join('\n')+'\n');
const silent = path.join(out,'silent.mp4');
run('ffmpeg',['-y','-loglevel','error','-f','concat','-safe','0','-i',concat,'-c','copy',silent]);
if (duration(silent) < b[5] - 0.15) throw new Error('Der Bildschnitt ist unvollständig.');

async function elevenSfx(name, text, seconds) {
  if (!key || process.env.REEL_SKIP_SFX_API) return null;
  const response = await fetch('https://api.elevenlabs.io/v1/sound-generation', {
    method:'POST', headers:{'xi-api-key':key,'Content-Type':'application/json'},
    body:JSON.stringify({text,duration_seconds:seconds,prompt_influence:.55,model_id:'eleven_text_to_sound_v2'})
  });
  if (!response.ok) { console.warn(`SFX ${name}: ElevenLabs ${response.status}: ${(await response.text()).slice(0,150)}`); return null; }
  const target = path.join(out,`${name}-elevenlabs.mp3`);
  fs.writeFileSync(target,Buffer.from(await response.arrayBuffer()));
  return target;
}
let impact = await elevenSfx('impact','A single sharp clank of a solid stainless steel travel mug hitting a hard helmet visor, short brittle glass crack and metallic ringing tail. Clean isolated foley, no speech, no music, no ambience.',1.7);
let scanner = await elevenSfx('scanner','One brief clean futuristic electronic scan sweep followed by a soft two note confirmation ping. Isolated sound effect, no voice, no music, no ambience.',1.25);
if (!impact) impact = process.env.REEL_IMPACT_PATH || null;
if (!scanner) scanner = process.env.REEL_SCANNER_PATH || null;
if (!impact) {
  impact = path.join(out,'impact-synth.wav');
  run('ffmpeg',['-y','-loglevel','error','-f','lavfi','-i','anoisesrc=color=brown:duration=0.65:amplitude=0.7','-af','highpass=f=200,lowpass=f=4200,afade=t=out:st=0.04:d=0.58','-ar','48000',impact]);
}
if (!scanner) {
  scanner = path.join(out,'scanner-synth.wav');
  run('ffmpeg',['-y','-loglevel','error','-f','lavfi','-i','sine=frequency=950:duration=0.55','-af','afade=t=in:st=0:d=0.03,afade=t=out:st=0.19:d=0.35,volume=0.5','-ar','48000',scanner]);
}
const ms = t => Math.max(0,Math.round(t*1000));
const audioFilter = `[1:a]loudnorm=I=-16:TP=-1.5:LRA=11[v];`+
  `[2:a]volume=0.30,adelay=${ms(beats[1].at)}:all=1[h1];`+
  `[2:a]volume=0.17,adelay=${ms(beats[7].at)}:all=1[h2];`+
  `[3:a]volume=0.16,adelay=${ms(beats[5].at)}:all=1[s1];`+
  `[3:a]volume=0.12,adelay=${ms(beats[9].at)}:all=1[s2];`+
  `[v][h1][h2][s1][s2]amix=inputs=5:duration=longest:normalize=0,alimiter=limit=0.9[a]`;
const destination = path.join(out,'herrjurist-224-test-v3.mp4');
run('ffmpeg',['-y','-loglevel','error','-i',silent,'-i',voicePath,'-i',impact,'-i',scanner,'-filter_complex',audioFilter,'-map','0:v:0','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-t',String(b[5]),'-movflags','+faststart',destination]);
fs.writeFileSync(path.join(out,'timing.json'),JSON.stringify({voice,model,voiceDuration,boundaries:b,images:beats.map(x=>({at:x.at,until:x.until,image:x.image,punch:x.punch||1})),impact,scanner},null,2));
console.log(`Fertig: ${destination}; ${b[5].toFixed(2)} s; ${impact}; ${scanner}`);
