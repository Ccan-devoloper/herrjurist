import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const dir = path.resolve('reel-test-2026-09-27');
const out = path.join(dir, 'out');
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
if (!key) throw new Error('ELEVENLABS_API_KEY fehlt: ElevenLabs-Test kann nicht gesprochen werden.');
const voice = process.env.ELEVENLABS_VOICE_ID || 'PhufIH7nYh2Up1uej6aY';
const model = process.env.ELEVENLABS_MODEL || 'eleven_multilingual_v2';
const response = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${encodeURIComponent(voice)}/with-timestamps?output_format=mp3_44100_128`, {
  method: 'POST',
  headers: { 'xi-api-key': key, 'Content-Type': 'application/json' },
  body: JSON.stringify({ text: script, model_id: model, language_code: 'de', voice_settings: { stability: 0.42, similarity_boost: 0.8, style: 0.36, use_speaker_boost: true, speed: 1.06 } })
});
if (!response.ok) throw new Error(`ElevenLabs ${response.status}: ${(await response.text()).slice(0, 240)}`);
const spoken = await response.json();
const voicePath = path.join(out, 'sprecher-elevenlabs.mp3');
fs.writeFileSync(voicePath, Buffer.from(spoken.audio_base64, 'base64'));
function run(command, args) {
  const result = spawnSync(command, args, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
  if (result.status !== 0) throw new Error(`${command} fehlgeschlagen: ${result.stderr.slice(-3000)}`);
  return result.stdout.trim();
}
const rawDuration = Number(run('ffprobe', ['-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',voicePath]));
const speed = rawDuration > 27.1 ? rawDuration / 27.1 : 1;
const adjustedVoice = path.join(out, 'sprecher.mp3');
if (speed > 1) run('ffmpeg', ['-y','-loglevel','error','-i',voicePath,'-af',`atempo=${speed.toFixed(4)}`,'-q:a','2',adjustedVoice]);
else fs.copyFileSync(voicePath, adjustedVoice);
const voiceDuration = rawDuration / speed;
const ends = spoken.alignment?.character_end_times_seconds || spoken.normalized_alignment?.character_end_times_seconds || [];
let character = 0;
const boundaries = lines.map((line, i) => {
  character += line.length;
  const fallback = rawDuration * character / script.length;
  const t = Number.isFinite(ends[character - 1]) ? ends[character - 1] : fallback;
  character += i < lines.length - 1 ? 1 : 0;
  return t / speed;
});
const cuts = [0, ...boundaries.slice(0, -1).map((t, i) => Math.max(t + 0.1, (i ? boundaries[i - 1] / speed : 0) + 2.0)), voiceDuration + 0.55];
// The final cut always covers all spoken audio and gives the visual payoff a short hold.
for (let i = 1; i < cuts.length - 1; i++) cuts[i] = Math.min(cuts[i], voiceDuration - (cuts.length - i - 1) * 2.1);
const segments = [];
const font = path.resolve('fonts/Inter.ttf');
for (let i = 0; i < 5; i++) {
  const duration = Math.max(2.05, cuts[i + 1] - cuts[i]);
  const input = path.join(dir, 'shots', `shot-${String(i + 1).padStart(2, '0')}.jpg`);
  const output = path.join(out, `segment-${String(i + 1).padStart(2, '0')}.mp4`);
  const fps = 30;
  const frames = Math.ceil(duration * fps);
  let filter = `scale=1080:1920,zoompan=z='min(zoom+0.00020,1.045)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=${fps},format=yuv420p`;
  if (i === 0) filter += `,drawtext=fontfile=${font}:text='Ein Becher?':fontsize=76:fontcolor=white:borderw=4:bordercolor=black:box=1:boxcolor=black@0.58:boxborderw=20:x=(w-text_w)/2:y=250`;
  if (i === 4) filter += `,drawtext=fontfile=${font}:text='§ 224 I Nr. 2':fontsize=70:fontcolor=white:borderw=4:bordercolor=black:box=1:boxcolor=black@0.58:boxborderw=20:x=(w-text_w)/2:y=260`;
  run('ffmpeg', ['-y','-loglevel','error','-loop','1','-framerate',String(fps),'-i',input,'-vf',filter,'-frames:v',String(frames),'-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-an',output]);
  segments.push({ input, output, start: cuts[i], duration, frames });
}
const concat = path.join(out, 'concat.txt');
fs.writeFileSync(concat, segments.map(s => `file '${s.output.replaceAll("'", "'\\''")}'`).join('\n') + '\n');
const silent = path.join(out, 'silent.mp4');
run('ffmpeg',['-y','-loglevel','error','-f','concat','-safe','0','-i',concat,'-c','copy',silent]);
const destination = path.join(out,'herrjurist-224-microstory-test.mp4');
run('ffmpeg',['-y','-loglevel','error','-i',silent,'-i',adjustedVoice,'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-af','loudnorm=I=-16:TP=-1.5:LRA=11','-t',String(cuts.at(-1)),'-movflags','+faststart',destination]);
fs.writeFileSync(path.join(out,'timing.json'),JSON.stringify({topic:'§ 224 Abs. 1 Nr. 2 StGB',voice,model,script,rawDuration,voiceDuration,cuts,segments:segments.map(({start,duration,frames})=>({start,duration,frames}))},null,2));
console.log(`Fertig: ${destination}; ${cuts.at(-1).toFixed(2)} s; ElevenLabs ${voice}/${model}`);
