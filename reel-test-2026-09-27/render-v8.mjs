import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const dir = path.resolve('reel-test-2026-09-27');
const out = path.join(dir, 'out-v8');
fs.mkdirSync(out, { recursive: true });
const lines = [
  'Rex schlägt Mara mit einem Thermobecher.',
  'Gefährliche Körperverletzung? Ein Becher ist doch keine Waffe.',
  'Aber bei Paragraf zweihundertvierundzwanzig zählt der konkrete Einsatz.',
  'Harter Becher, voller Schwung, Treffer am Kopf: Kann das erhebliche Verletzungen verursachen?',
  'Dann kann er ein gefährliches Werkzeug sein. Merke: Beschaffenheit und Verwendung prüfen.'
];
const script = lines.join(' ');
const approvedDir = path.join(dir,'audio-v5');
const approvedTiming = fs.existsSync(path.join(approvedDir,'timing.json')) ? JSON.parse(fs.readFileSync(path.join(approvedDir,'timing.json'),'utf8')) : null;
if (approvedTiming && approvedTiming.script !== script) throw new Error('Freigegebene Audiofassung passt nicht zum Skript.');
const key = process.env.ELEVENLABS_API_KEY;
const voice = process.env.ELEVENLABS_VOICE_ID || 'PhufIH7nYh2Up1uej6aY';
const model = process.env.ELEVENLABS_MODEL || 'eleven_multilingual_v2';
function run(command, args) {
  const result = spawnSync(command, args, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
  if (result.status !== 0) throw new Error(`${command}: ${result.stderr.slice(-2000)}`);
  return result.stdout.trim();
}
function duration(file) { return Number(run('ffprobe', ['-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',file])); }

let voicePath = process.env.REEL_VOICE_PATH || (approvedTiming ? path.join(approvedDir,'sprecher.mp3') : null);
let alignment;
let startTimes;
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
  startTimes = spoken.alignment?.character_start_times_seconds || spoken.normalized_alignment?.character_start_times_seconds;
}
const voiceDuration = duration(voicePath);
let char = 0;
const boundaries = lines.map((line, i) => {
  char += line.length;
  const seconds = alignment?.[char - 1] ?? voiceDuration * char / script.length;
  if (i < lines.length - 1) char++;
  return Math.min(voiceDuration, seconds);
});
const lead = approvedTiming?.lead ?? 0.52;
const base = approvedTiming?.boundaries ?? (alignment ? [0, ...boundaries.slice(0,4).map(t=>t+lead), voiceDuration+lead+0.18] :
  [0,2.136,6.316,10.542,16.985,voiceDuration+0.18].map((t,i)=>i? t+lead : 0));
const b = base;
const merkeIndex = script.indexOf('Merke:');
const exactMerke = startTimes?.[merkeIndex];
const merkeAt = approvedTiming?.merkeAt ?? (Number.isFinite(exactMerke) ? exactMerke + lead : b[4]+(b[5]-b[4])*.53);
const fps = 30;
const contact = b[3]+(b[4]-b[3])*.33;
const closeEnd = b[3]+(b[4]-b[3])*.70;
const anticipation = contact-7/fps;
const impactEnd = contact+2/fps;
const holdEnd = impactEnd+11/fps;
const beats = [
  {at:0, until:.42, image:'shot-01.jpg'},
  {at:.42, until:b[1], image:'shot-01.jpg', punch:1.13, textStyle:'hook'},
  {at:b[1], until:b[1]+(b[2]-b[1])*.59, image:'shot-06-aftermath.jpg'},
  {at:b[1]+(b[2]-b[1])*.59, until:b[2], image:'shot-03.jpg'},
  {at:b[2], until:b[2]+(b[3]-b[2])*.53, image:'shot-09-rule.jpg'},
  {at:b[2]+(b[3]-b[2])*.53, until:b[3], image:'shot-07-mug-scan.jpg'},
  {at:b[3], until:anticipation, image:'shot-04.jpg'},
  {at:anticipation, until:contact, image:'shot-12-anticipation.jpg'},
  {at:contact, until:impactEnd, image:'shot-13-impact-frame.jpg'},
  {at:impactEnd, until:holdEnd, image:'shot-08-impact-close.jpg'},
  {at:holdEnd, until:closeEnd, image:'shot-14-reaction.jpg'},
  {at:closeEnd, until:b[4], image:'shot-06-aftermath.jpg'},
  {at:b[4], until:merkeAt, image:'shot-11-law-projection.jpg', textStyle:'law'},
  {at:merkeAt, until:b[5], image:'shot-10-mnemonic.jpg', textStyle:'mnemonic'}
];
if (merkeAt <= b[4]+.8 || merkeAt >= b[5]-.8) throw new Error(`Merke-Schnitt außerhalb der letzten Zeile: ${merkeAt}`);
const comicFont = path.resolve('fonts/Anton.ttf');
const hudFont = path.resolve('fonts/SpaceGrotesk.ttf');
for (let i = 0; i < beats.length; i++) {
  const beat = beats[i];
  const input = path.join(dir, 'shots', beat.image);
  const output = path.join(out, `scene-${String(i+1).padStart(2,'0')}.mp4`);
  const punch = beat.punch || 1;
  const w = Math.round(1080 * punch / 2) * 2;
  const h = Math.round(1920 * punch / 2) * 2;
  // These dimensions and crop offsets are fixed for every frame: no zoompan or per-frame motion.
  const baseFilter = `scale=${w}:${h}:force_original_aspect_ratio=increase,crop=1080:1920:(iw-1080)/2:(ih-1920)/2,format=rgba`;
  const sticker = beat.textStyle==='hook' ? path.join(dir,'overlays','comic-burst.webp') : null;
  let filter = `[0:v]${baseFilter}[bg]`;
  if (sticker) filter += `;[1:v]scale=970:323[st];[bg][st]overlay=x=(W-w)/2:y=230[card]`;
  else filter += `;[bg]null[card]`;
  if (beat.textStyle==='hook') filter += `;[card]drawtext=fontfile=${comicFont}:text='BECHER ALS WAFFE?':fontsize=105:fontcolor=0x182932:borderw=2:bordercolor=0xfff0bc:shadowcolor=0xd45e16@0.7:shadowx=3:shadowy=4:x=(w-text_w)/2:y=335,format=yuv420p[v]`;
  else if (beat.textStyle==='law') filter += `;[card]drawtext=fontfile=${comicFont}:text='§ 224':fontsize=170:fontcolor=0x162f3c:borderw=3:bordercolor=white@0.9:shadowcolor=0x16deee@0.6:shadowx=3:shadowy=4:x=(w-text_w)/2:y=202,drawtext=fontfile=${comicFont}:text='I NR. 2 STGB':fontsize=79:fontcolor=0x162f3c:borderw=2:bordercolor=white@0.9:x=(w-text_w)/2:y=391,format=yuv420p[v]`;
  else if (beat.textStyle==='mnemonic') filter += `;[card]drawtext=fontfile=${comicFont}:text='§ 224 I NR. 2 STGB':fontsize=86:fontcolor=white:borderw=2:bordercolor=0x075b70:shadowcolor=0x00ddf5@0.7:shadowx=2:shadowy=2:x=(w-text_w)/2:y=210,drawtext=fontfile=${hudFont}:text='BESCHAFFENHEIT':fontsize=54:fontcolor=white:borderw=1:bordercolor=0x03667b:x=282-text_w/2:y=670,drawtext=fontfile=${hudFont}:text='VERWENDUNG':fontsize=58:fontcolor=white:borderw=1:bordercolor=0x03667b:x=805-text_w/2:y=670,format=yuv420p[v]`;
  else filter += `;[card]format=yuv420p[v]`;
  const args = ['-y','-loglevel','error','-loop','1','-framerate',String(fps),'-i',input];
  if(sticker) args.push('-loop','1','-framerate',String(fps),'-i',sticker);
  args.push('-filter_complex',filter,'-map','[v]','-frames:v',String(Math.round((beat.until-beat.at)*fps)),'-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-an',output);
  run('ffmpeg', args);
  beat.encodeArgs = args;
  beat.output = output;
}
// Verify every file after the whole batch, since a truncated MP4 would stop concat early.
let actualAt = 0;
for (const beat of beats) {
  let ok = false;
  for (let attempt = 0; attempt < 3 && !ok; attempt++) {
    try { ok = fs.statSync(beat.output).size > 1000 && duration(beat.output) >= 1/fps-.001; } catch {}
    if (!ok) run('ffmpeg', beat.encodeArgs);
  }
  if (!ok) throw new Error(`Leeres Segment: ${beat.output}`);
  beat.actualAt = actualAt;
  actualAt += duration(beat.output);
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
    body:JSON.stringify({text,duration_seconds:seconds,prompt_influence:.7,model_id:'eleven_text_to_sound_v2'})
  });
  if (!response.ok) { console.warn(`SFX ${name}: ElevenLabs ${response.status}: ${(await response.text()).slice(0,150)}`); return null; }
  const target = path.join(out,`${name}-elevenlabs.mp3`);
  fs.writeFileSync(target,Buffer.from(await response.arrayBuffer()));
  return target;
}
let impact = approvedTiming ? path.join(approvedDir,'impact.mp3') : await elevenSfx('impact','One VERY LOUD sharp explosive WHACK as a heavy solid stainless steel travel mug violently strikes a hard helmet visor. Bright crunchy midrange impact and a brief metal snap, immediate attack, short tail. Not soft, not muffled, no bass boom, no gentle clink, no speech, no music.',0.85);
let crack = approvedTiming ? path.join(approvedDir,'crack.mp3') : await elevenSfx('crack','One short high-energy brittle visor CRACK at the instant of a hard blow, with a tiny rattling shard tail. Sharp close microphone sound, no deep thud, no bell or chime, no speech, no music.',0.68);
// Maras kräftiger Eleven-v3-Aufschrei liegt nur auf dem gezeichneten Kontakt und der Reaktion.
let yelp = path.join(dir,'audio-v7','mara-close-cry.mp3');
let scanner = approvedTiming ? path.join(approvedDir,'scanner.mp3') : await elevenSfx('scanner','One short clean futuristic evidence scan ping, quiet and precise, no voice, no music, no ambience.',0.7);
if (!impact) impact = process.env.REEL_IMPACT_PATH || null;
if (!crack) crack = process.env.REEL_CRACK_PATH || null;
if (!scanner) scanner = process.env.REEL_SCANNER_PATH || null;
if (!impact || !crack || !yelp) throw new Error('Schlag, Visierknacken oder Maras Aufschrei fehlt.');
if (!scanner) {
  scanner = path.join(out,'scanner-synth.wav');
  run('ffmpeg',['-y','-loglevel','error','-f','lavfi','-i','sine=frequency=950:duration=0.55','-af','afade=t=in:st=0:d=0.03,afade=t=out:st=0.19:d=0.35,volume=0.5','-ar','48000',scanner]);
}
const ms = t => Math.max(0,Math.round(t*1000));
const replay = beats[6].actualAt;
const closeHit = beats[8].actualAt;
const audioFilter = `[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,adelay=${ms(lead)}:all=1,volume=0.7:enable='between(t,${(closeHit-.14).toFixed(3)},${(closeHit+1.5).toFixed(3)})'[v];`+
  `[2:a]highpass=f=160,equalizer=f=1850:t=q:w=1.4:g=7,volume=3.1,adelay=0:all=1[h1];`+
  `[2:a]highpass=f=160,equalizer=f=1850:t=q:w=1.4:g=7,volume=1.8,adelay=${ms(replay)}:all=1[h2];`+
  `[2:a]highpass=f=160,equalizer=f=1850:t=q:w=1.4:g=7,volume=1.45,adelay=${ms(closeHit)}:all=1[h3];`+
  `[3:a]atrim=start=0.10,asetpts=PTS-STARTPTS,highpass=f=550,volume=0.95,adelay=10:all=1[c1];`+
  `[3:a]atrim=start=0.10,asetpts=PTS-STARTPTS,highpass=f=550,volume=0.55,adelay=${ms(replay)+10}:all=1[c2];`+
  `[3:a]atrim=start=0.10,asetpts=PTS-STARTPTS,highpass=f=550,volume=0.70,adelay=${ms(closeHit)+10}:all=1[c3];`+
  `[4:a]atrim=start=0.055,asetpts=PTS-STARTPTS,highpass=f=190,volume=0.90,adelay=${ms(closeHit)+10}:all=1[y];`+
  `[5:a]volume=0.13,adelay=${ms(beats[5].at)}:all=1[s];`+
  `[v][h1][h2][h3][c1][c2][c3][y][s]amix=inputs=9:duration=longest:normalize=0,alimiter=limit=0.86[a]`;
const destination = path.join(out,'herrjurist-224-test-v8.mp4');
const mixArgs = ['-y','-loglevel','error','-i',silent,'-i',voicePath,'-i',impact,'-i',crack,'-i',yelp,'-i',scanner,'-filter_complex',audioFilter,'-map','0:v:0','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-t',String(b[5]),'-movflags','+faststart',destination];
let mixed = false;
for (let attempt=0; attempt<3 && !mixed; attempt++) {
  run('ffmpeg',mixArgs);
  try { mixed=fs.statSync(destination).size>1000000 && duration(destination)>b[5]-0.15; } catch {}
}
if (!mixed) throw new Error('Fertige MP4 ist unvollständig.');
fs.writeFileSync(path.join(out,'timing.json'),JSON.stringify({voice,model,script,voiceDuration,lead,boundaries:b,merkeAt,closeHit,images:beats.map(x=>({at:x.at,actualAt:x.actualAt,until:x.until,image:x.image,punch:x.punch||1,textStyle:x.textStyle||null})),impact,crack,yelp,scanner,maraVoice:'Selena / Eleven v3, German, middle-aged'},null,2));
console.log(`Fertig: ${destination}; ${b[5].toFixed(2)} s; Merke bei ${merkeAt.toFixed(2)} s`);
