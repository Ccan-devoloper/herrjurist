import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';

const root = path.resolve('reel-2026-10-01');
const out = path.join(root, 'out');
const audio = path.join(root, 'audio');
for (const dir of [out, audio]) fs.mkdirSync(dir, {recursive: true});
const key = process.env.ELEVENLABS_API_KEY;
if (!key) throw Error('ELEVENLABS_API_KEY fehlt');
const voices = {
  narrator: 'PhufIH7nYh2Up1uej6aY', // Moritz, freigegebene Erzählerstimme
  mara: '2aL479c8D3QMIPExj0tw'      // Selena, bereits für Mara etabliert
};
const lines = [
  'Alle Instanzen durch. Karlsruhe bleibt trotzdem zu. Warum?',
  'Zurück. Mara hätte den Grundrechtsverstoß schon beim Fachgericht rügen können.',
  'Sie schwieg.',
  'Paragraf neunzig Absatz zwei Satz eins verlangt Rechtswegerschöpfung.',
  'Subsidiarität verlangt darüber hinaus, zumutbare Möglichkeiten vor den Fachgerichten zu nutzen.',
  'Ein ausgeschöpfter Rechtsweg öffnet nicht beide Türen. In der Klausur: beide Hürden getrennt prüfen.'
];
const script = lines.join(' ');
const maraText = '[frustrated] Aber ich war doch überall!';
const maraWords = 'Aber ich war doch überall!';

function run(command, args) {
  const r = spawnSync(command, args, {encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'pipe'], maxBuffer: 64 * 1024 * 1024});
  if (r.status !== 0) throw Error(command + ': ' + r.stderr.slice(-5000));
  return r.stdout.trim();
}
const duration = p => Number(run('ffprobe',
  ['-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',p]));

async function speak(name, voice, text, model, settings) {
  const p = path.join(audio, name + '.mp3');
  const j = path.join(audio, name + '.json');
  if (fs.existsSync(p) && fs.existsSync(j))
    return {p, data: JSON.parse(fs.readFileSync(j, 'utf8'))};
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' +
    voice + '/with-timestamps?output_format=mp3_44100_128', {
    method: 'POST',
    headers: {'xi-api-key': key, 'Content-Type': 'application/json'},
    body: JSON.stringify({text, model_id: model, language_code: 'de',
      voice_settings: settings})
  });
  if (!r.ok) throw Error(name + ': ElevenLabs ' + r.status + ': ' +
    (await r.text()).slice(0, 400));
  const data = await r.json();
  fs.writeFileSync(p, Buffer.from(data.audio_base64, 'base64'));
  fs.writeFileSync(j, JSON.stringify({text, voice, model,
    alignment: data.alignment,
    normalized_alignment: data.normalized_alignment}, null, 2));
  return {p, data: JSON.parse(fs.readFileSync(j, 'utf8'))};
}
const narrator = await speak('sprecher', voices.narrator, script,
  'eleven_multilingual_v2',
  {stability:.42,similarity_boost:.82,style:.38,
   use_speaker_boost:true,speed:1.08});
const mara = await speak('mara', voices.mara, maraText, 'eleven_v3',
  {stability:.38,similarity_boost:.78,style:.67,
   use_speaker_boost:true,speed:1.00});

function matchingAlignment(data, needle) {
  for (const a of [data.alignment, data.normalized_alignment])
    if (a?.characters?.join('') === needle) return a;
  throw Error('Alignment differs from narrator text');
}
function phraseWindow(data, phrase) {
  for (const a of [data.alignment, data.normalized_alignment]) {
    const i = a?.characters?.join('').indexOf(phrase) ?? -1;
    if (i >= 0) return {start:a.character_start_times_seconds[i],
      end:a.character_end_times_seconds[i + phrase.length - 1]};
  }
  throw Error('Phrase absent from alignment: ' + phrase);
}
const A = matchingAlignment(narrator.data, script);
const M = phraseWindow(mara.data, maraWords);
const starts = [], ends = [];
let offset = 0;
for (const line of lines) {
  starts.push(offset); offset += line.length; ends.push(offset - 1); offset++;
}
const lead = .20;
const split = A.character_end_times_seconds[ends[2]] + .04;
const gapStart = lead + split;
const maraAt = gapStart + .26;
const gap = .26 + M.end + .43;
const narratorGapped = path.join(audio, 'sprecher-mit-pause.wav');
const concat = '[0:a]atrim=end=' + split +
  ',asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=mono[a0];' +
  '[1:a]atrim=duration=' + gap +
  ',asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=mono[s];' +
  '[0:a]atrim=start=' + split +
  ',asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=mono[a1];' +
  '[a0][s][a1]concat=n=3:v=0:a=1[a]';
run('ffmpeg', ['-y','-loglevel','error','-i',narrator.p,
  '-f','lavfi','-t',String(gap),'-i','anullsrc=r=44100:cl=mono',
  '-filter_complex',concat,'-map','[a]','-c:a','pcm_s16le',narratorGapped]);
const startAt = i => lead + A.character_start_times_seconds[i] +
  (i > ends[2] ? gap : 0);
const endAt = i => lead + A.character_end_times_seconds[i] +
  (i > ends[2] ? gap : 0);
const lineStart = i => startAt(starts[i]);
const lineEnd = i => endAt(ends[i]);
const finalDuration = Math.max(lineEnd(5) + .55, maraAt + M.end + .5);
if (finalDuration > 30.15) throw Error('Over 30 seconds: ' +
  finalDuration.toFixed(2) + '. Tighten the script before approval.');
const events = {
  door_close_at: startAt(script.indexOf('bleibt')),
  intro_end: lineEnd(0) + .10,
  silence_at: lineStart(2),
  return_at: gapStart + .08,
  evidence_at: maraAt + M.end - .08,
  law_at: lineStart(3) + .85,
  reaction_at: lineStart(3) + 3.35,
  two_hurdles_at: lineStart(4) + 2.25,
  pointe_at: lineStart(5) + 1.75
};
const order = ['door_close_at','intro_end','silence_at','return_at',
  'evidence_at','law_at','reaction_at','two_hurdles_at','pointe_at'];
for (let i = 1; i < order.length; i++)
  if (!(events[order[i-1]] < events[order[i]]))
    throw Error('Bad scene order: ' + JSON.stringify(events));
if (!(events.pointe_at < finalDuration - .6))
  throw Error('Final pose too brief: ' + JSON.stringify(events));

function stamp(t) {
  const c = Math.round(Math.max(0,t) * 100);
  return Math.floor(c / 360000) + ':' +
    String(Math.floor(c / 6000) % 60).padStart(2,'0') + ':' +
    String(Math.floor(c / 100) % 60).padStart(2,'0') + '.' +
    String(c % 100).padStart(2,'0');
}
let ass = '[Script Info]\nTitle: Herr Jurist 01 October review\n' +
  'ScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n' +
  'WrapStyle: 2\nScaledBorderAndShadow: yes\n\n' +
  '[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, ' +
  'SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, ' +
  'StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, ' +
  'Alignment, MarginL, MarginR, MarginV, Encoding\n' +
  'Style: Phrase,Nimbus Sans,72,&H00FAFAFA&,&H00FAFAFA&,&H00191919&,' +
  '&H90000000&,-1,0,0,0,100,100,0,0,1,2.5,2,2,110,170,280,1\n\n' +
  '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, ' +
  'MarginV, Effect, Text\n';
function caption(start, end, shown) {
  const size = shown.length > 29 ? 55 : shown.length > 20 ? 64 : 72;
  ass += 'Dialogue: 0,' + stamp(start) + ',' +
    stamp(Math.max(end,start+.15)) +
    ',Phrase,,0,0,0,,{\\fs' + size + '\\fad(70,70)}' + shown + '\n';
}
const phrases = [
  ['Alle Instanzen durch.'], ['Karlsruhe bleibt'], ['trotzdem zu.'], ['Warum?'],
  ['Zurück.'], ['Mara hätte den'], ['Grundrechtsverstoß schon'],
  ['beim Fachgericht rügen können.'], ['Sie schwieg.'],
  ['Paragraf neunzig Absatz zwei Satz eins','§ 90 Abs. 2 S. 1'],
  ['verlangt Rechtswegerschöpfung.'],
  ['Subsidiarität verlangt'], ['darüber hinaus,'],
  ['zumutbare Möglichkeiten'], ['vor den Fachgerichten'], ['zu nutzen.'],
  ['Ein ausgeschöpfter Rechtsweg'], ['öffnet nicht beide Türen.'],
  ['In der Klausur:'], ['beide Hürden getrennt prüfen.']
];
if (phrases.map(p => p[0]).join(' ').replace(/\s/g,'') !==
    script.replace(/\s/g,'')) throw Error('Narrator caption coverage differs');
const rows = [];
let cursor = 0;
for (const [spoken, shown = spoken] of phrases) {
  const first = script.indexOf(spoken, cursor);
  if (first < cursor) throw Error('Caption phrase missing: ' + spoken);
  const last = first + spoken.length - 1;
  rows.push({start:startAt(first), end:endAt(last)+.05, shown});
  cursor = last + 1;
}
for (let i = 0; i < rows.length; i++) {
  const next = rows[i+1] ? rows[i+1].start - .02 : Infinity;
  caption(rows[i].start, Math.min(rows[i].end, next), rows[i].shown);
}
caption(maraAt + M.start, maraAt + M.end + .08, maraWords);
fs.writeFileSync(path.join(out,'untertitel-sinngruppen.ass'), ass);

const effects = [
  {name:'gate', at:events.door_close_at, volume:.43, seconds:1.1,
   prompt:'A massive futuristic stone-and-steel courthouse portal slams shut abruptly: loud clean metallic CLANG with short low resonance and small electric latch click; one impact, no voice or music.'},
  {name:'rewind', at:events.intro_end+.03, volume:.23, seconds:.9,
   prompt:'One short cinematic backward page-and-clock whoosh into a court hearing flashback, dry and clear, no voices or music.'},
  {name:'courtroom', at:events.intro_end+.4, volume:.045, seconds:5,
   prompt:'Quiet futuristic lower courthouse hearing room ambience: faint ventilation, paper rustle, no voices, no music, restrained loop.'},
  {name:'file-close', at:events.silence_at, volume:.24, seconds:.8,
   prompt:'A thick beige legal dossier closes on a courthouse desk with a decisive dry paper thump, tiny page flutter, no speech or music.'},
  {name:'page-reveal', at:events.evidence_at, volume:.22, seconds:.7,
   prompt:'Quick tactile page turn and a small precise robotic pointing click over a case file, light and dry, no voice or music.'},
  {name:'law', at:events.law_at, volume:.15, seconds:.9,
   prompt:'Restrained mint-green legal projection from a small robot clipboard onto stone wall: one clean soft electronic rise and lock-in, no voice or music.'},
  {name:'latch', at:events.two_hurdles_at, volume:.30, seconds:1.0,
   prompt:'A huge courthouse second gate refuses access with a firm mechanical latch clack and short restrained electronic deny pulse; no speech, no music.'}
];
for (const e of effects) {
  e.path = path.join(audio,e.name+'.mp3');
  if (fs.existsSync(e.path)) continue;
  const r = await fetch('https://api.elevenlabs.io/v1/sound-generation', {
    method:'POST',
    headers:{'xi-api-key':key,'Content-Type':'application/json'},
    body:JSON.stringify({text:e.prompt,duration_seconds:e.seconds,
      prompt_influence:.8,model_id:'eleven_text_to_sound_v2'})
  });
  if (!r.ok) throw Error(e.name+' SFX '+r.status+': '+(await r.text()).slice(0,300));
  fs.writeFileSync(e.path,Buffer.from(await r.arrayBuffer()));
}
const timing = {script,lines,lead,gap,events,
  final_duration:finalDuration,fps:30,voices,mara_text:maraWords,
  mara_at:maraAt,effects:effects.map(({path:unused,...rest})=>rest)};
fs.writeFileSync(path.join(out,'timing.json'),JSON.stringify(timing,null,2));
run('python3',[path.join(root,'make_frames.py'),'--timing',
  path.join(out,'timing.json'),'--out',path.join(out,'silent.mp4')]);
const ms = t => Math.round(Math.max(0,t)*1000);
const filters = [
  '[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,volume=.84[narrator]',
  '[2:a]highpass=f=95,volume=1.12,adelay='+ms(maraAt)+':all=1[mara]'
];
effects.forEach((e,i)=>filters.push('['+(i+3)+':a]highpass=f=90,volume='+
  e.volume+',adelay='+ms(e.at)+':all=1[s'+i+']'));
filters.push('[narrator][mara]'+effects.map((_,i)=>'[s'+i+']').join('')+
  'amix=inputs='+(effects.length+2)+
  ':duration=longest:normalize=0,alimiter=limit=0.94,apad[a]');
const dest = path.join(out,'herrjurist-2026-10-01-subsidiaritaet-review.mp4');
run('ffmpeg',['-y','-loglevel','error','-i',path.join(out,'silent.mp4'),
  '-i',narratorGapped,'-i',mara.p,
  ...effects.flatMap(e=>['-i',e.path]),
  '-filter_complex',filters.join(';'),'-map','0:v:0','-map','[a]',
  '-vf','ass='+path.join(out,'untertitel-sinngruppen.ass'),
  '-c:v','libx264','-preset','medium','-crf','19','-pix_fmt','yuv420p',
  '-r','30','-c:a','aac','-b:a','192k','-ar','48000',
  '-t',String(finalDuration),'-movflags','+faststart',dest]);
if (fs.statSync(dest).size<1_000_000 ||
    Math.abs(duration(dest)-finalDuration)>.20)
  throw Error('Incomplete export');
run('ffmpeg',['-y','-loglevel','error','-ss',String(events.door_close_at+.36),
  '-i',dest,'-frames:v','1','-q:v','3',path.join(out,'cover.jpg')]);
console.log(dest+': '+duration(dest).toFixed(2)+' s, 30 fps, fixed camera cels, '+
  JSON.stringify(voices));
