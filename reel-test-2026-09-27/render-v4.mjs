import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const dir = path.resolve('reel-test-2026-09-27');
const out = path.join(dir, 'out-v4');
fs.mkdirSync(out, { recursive: true });
const lines = [
  'Ein Becher als Waffe?',
  'Rex schlägt Mara damit gegen den Kopf.',
  'Bei Paragraf zweihundertvierundzwanzig zählt der konkrete Einsatz.',
  'Hartes Metall, voller Schwung: Kann das erheblich verletzen?',
  'Dann kann der Becher ein gefährliches Werkzeug sein.',
  'Merke: Beschaffenheit und Verwendung.'
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
const base = [0, ...boundaries.slice(0,-1), voiceDuration + 0.18];
const b = base;
const beats = [
  {at:0, until:Math.min(.60,b[1]*.48), image:'shot-01.jpg', label:'EIN BECHER', textStyle:'hook'},
  {at:Math.min(.60,b[1]*.48), until:b[1], image:'shot-01.jpg', punch:1.16, label:'ALS WAFFE?', textStyle:'hook'},
  {at:b[1], until:b[1]+(b[2]-b[1])*.58, image:'shot-06-aftermath.jpg'},
  {at:b[1]+(b[2]-b[1])*.58, until:b[2], image:'shot-03.jpg'},
  {at:b[2], until:b[2]+(b[3]-b[2])*.53, image:'shot-09-rule.jpg'},
  {at:b[2]+(b[3]-b[2])*.53, until:b[3], image:'shot-07-mug-scan.jpg'},
  {at:b[3], until:b[3]+(b[4]-b[3])*.52, image:'shot-04.jpg'},
  {at:b[3]+(b[4]-b[3])*.52, until:b[4], image:'shot-08-impact-close.jpg'},
  {at:b[4], until:b[5], image:'shot-05.jpg', textStyle:'statute'},
  {at:b[5], until:b[6], image:'shot-10-mnemonic.jpg', textStyle:'mnemonic'}
];
const headlineFont = path.resolve('fonts/Anton.ttf');
const hudFont = path.resolve('fonts/SpaceGrotesk.ttf');
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
  if (beat.textStyle === 'hook') filter += `,drawtext=fontfile=${headlineFont}:text='${beat.label}':fontsize=${beat.label.startsWith('EIN')?108:124}:fontcolor=0x172c39:borderw=3:bordercolor=0xffe6bc:shadowcolor=0x713218@0.55:shadowx=4:shadowy=5:x=(w-text_w)/2:y=285`;
  if (beat.textStyle === 'statute') filter += `,drawtext=fontfile=${hudFont}:text='§ 224 I Nr. 2 StGB':fontsize=44:fontcolor=white:borderw=1:bordercolor=0x06788a:shadowcolor=0x00dfff@0.7:shadowx=1:shadowy=1:x=(w-text_w)/2:y=307`;
  if (beat.textStyle === 'mnemonic') filter += `,drawtext=fontfile=${hudFont}:text='§ 224 I Nr. 2 StGB':fontsize=45:fontcolor=white:borderw=1:bordercolor=0x06788a:shadowcolor=0x00dfff@0.7:shadowx=1:shadowy=1:x=(w-text_w)/2:y=210,drawtext=fontfile=${hudFont}:text='BESCHAFFENHEIT':fontsize=54:fontcolor=white:borderw=1:bordercolor=0x03667b:shadowcolor=0x00dfff@0.75:shadowx=1:shadowy=2:x=282-text_w/2:y=670,drawtext=fontfile=${hudFont}:text='VERWENDUNG':fontsize=58:fontcolor=white:borderw=1:bordercolor=0x03667b:shadowcolor=0x00dfff@0.75:shadowx=1:shadowy=2:x=805-text_w/2:y=670`;
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
if (duration(silent) < b[6] - 0.15) throw new Error('Der Bildschnitt ist unvollständig.');

async function elevenSfx(name, text, seconds) {
  if (!key || process.env.REEL_SKIP_SFX_API) return null;
  const response = await fetch('https://api.elevenlabs.io/v1/sound-generation', {
    method:'POST', headers:{'xi-api-key':key,'Content-Type':'application/json'},
    body:JSON.stringify({text,duration_seconds:seconds,prompt_influence:.68,model_id:'eleven_text_to_sound_v2'})
  });
  if (!response.ok) { console.warn(`SFX ${name}: ElevenLabs ${response.status}: ${(await response.text()).slice(0,150)}`); return null; }
  const target = path.join(out,`${name}-elevenlabs.mp3`);
  fs.writeFileSync(target,Buffer.from(await response.arrayBuffer()));
  return target;
}
let body = await elevenSfx('body','One single immediate, powerful dry low-mid blunt WHACK of a heavy solid stainless steel travel mug against a helmet. Close recorded impact foley, forceful attack, very short tail. No delicate ringing, no speech, no music, no ambience.',0.85);
let crack = await elevenSfx('visor','One single sharp brittle CRACK of a hard transparent helmet visor under a heavy blow, followed by only a brief metallic rattle. Close impact foley, no soft chime, no speech, no music, no ambience.',0.70);
let scanner = await elevenSfx('scanner','One short clean electronic evidence scan ping, restrained and precise, no voice, no music, no ambience.',0.75);
if (!body) body = process.env.REEL_IMPACT_PATH || null;
if (!crack) crack = process.env.REEL_CRACK_PATH || process.env.REEL_IMPACT_PATH || null;
if (!scanner) scanner = process.env.REEL_SCANNER_PATH || null;
if (!body) {
  body = path.join(out,'body-synth.wav');
  run('ffmpeg',['-y','-loglevel','error','-f','lavfi','-i','anoisesrc=color=brown:duration=0.45:amplitude=0.7','-af','highpass=f=100,lowpass=f=1500,afade=t=out:st=0.02:d=0.4','-ar','48000',body]);
}
if (!crack) {
  crack = path.join(out,'visor-synth.wav');
  run('ffmpeg',['-y','-loglevel','error','-f','lavfi','-i','anoisesrc=color=white:duration=0.25:amplitude=0.4','-af','highpass=f=950,afade=t=out:st=0.015:d=0.23','-ar','48000',crack]);
}
if (!scanner) {
  scanner = path.join(out,'scanner-synth.wav');
  run('ffmpeg',['-y','-loglevel','error','-f','lavfi','-i','sine=frequency=950:duration=0.55','-af','afade=t=in:st=0:d=0.03,afade=t=out:st=0.19:d=0.35,volume=0.5','-ar','48000',scanner]);
}
const thud = path.join(out,'low-thud.wav');
run('ffmpeg',['-y','-loglevel','error','-f','lavfi','-i','sine=frequency=135:sample_rate=48000:duration=0.25','-af','afade=t=out:st=0.025:d=0.22','-ar','48000',thud]);
const ms = t => Math.max(0,Math.round(t*1000));
const replay = beats[6].at;
const audioFilter = `[1:a]loudnorm=I=-16:TP=-1.5:LRA=11[v];`+
  `[2:a]volume=0.72,adelay=0:all=1[b1];`+
  `[2:a]volume=0.45,adelay=${ms(replay)}:all=1[b2];`+
  `[3:a]volume=0.38,adelay=18:all=1[c1];`+
  `[3:a]volume=0.24,adelay=${ms(replay)+18}:all=1[c2];`+
  `[4:a]volume=0.52,adelay=0:all=1[t1];`+
  `[4:a]volume=0.33,adelay=${ms(replay)}:all=1[t2];`+
  `[5:a]volume=0.12,adelay=${ms(beats[5].at)}:all=1[s1];`+
  `[v][b1][b2][c1][c2][t1][t2][s1]amix=inputs=8:duration=longest:normalize=0,alimiter=limit=0.88[a]`;
const destination = path.join(out,'herrjurist-224-test-v4.mp4');
run('ffmpeg',['-y','-loglevel','error','-i',silent,'-i',voicePath,'-i',body,'-i',crack,'-i',thud,'-i',scanner,'-filter_complex',audioFilter,'-map','0:v:0','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-t',String(b[6]),'-movflags','+faststart',destination]);
fs.writeFileSync(path.join(out,'timing.json'),JSON.stringify({voice,model,script,voiceDuration,boundaries:b,images:beats.map(x=>({at:x.at,until:x.until,image:x.image,punch:x.punch||1,textStyle:x.textStyle||null})),body,crack,scanner},null,2));
console.log(`Fertig: ${destination}; ${b[6].toFixed(2)} s; ${body}; ${crack}`);
