import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';

const root = path.resolve('reel-2026-09-30-v7');
const out = path.join(root, 'out'), audio = path.join(root, 'audio');
for (const dir of [out, audio]) fs.mkdirSync(dir, {recursive:true});
const key = process.env.ELEVENLABS_API_KEY;
if (!key) throw Error('ELEVENLABS_API_KEY fehlt');
const voices = {narrator:'PhufIH7nYh2Up1uej6aY',
                brakk:'JiW03c2Gt43XNUQAumRP',
                zylla:'xLCJR8xcZX2YjImGFyGw'};
const lines = [
  'Sie unterschreibt. Trotzdem ist ihr Geständnis unverwertbar. Warum?',
  'Zurück. Brakk hält Zylla die ganze Nacht wach.',
  'Sie nickt immer wieder weg.',
  'Er startet die Aufnahme.',
  'Später willigt sie in die Verwertung ein.',
  'Paragraf einhundertsechsunddreißig A verbietet Ermüdung als Vernehmungsmethode.',
  'Absatz drei: Auch ihre Einwilligung macht das Geständnis nicht verwertbar.'
];
const script = lines.join(' ');
const brakkText = 'Nicht einschlafen! Rede endlich!';
const zyllaText = '[exhausted, whispering] Ich war’s.';
const zyllaWords = 'Ich war’s.';

function run(command, args) {
  const r = spawnSync(command, args, {encoding:'utf8',
    stdio:['ignore','pipe','pipe'],maxBuffer:64*1024*1024});
  if (r.status !== 0) throw Error(command + ': ' + r.stderr.slice(-4500));
  return r.stdout.trim();
}
const duration = p => Number(run('ffprobe',
  ['-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',p]));

async function speak(name, voice, text, model, settings) {
  const p = path.join(audio, name + '.mp3'), j = path.join(audio, name + '.json');
  if (fs.existsSync(p) && fs.existsSync(j))
    return {p, data:JSON.parse(fs.readFileSync(j, 'utf8'))};
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' +
    voice + '/with-timestamps?output_format=mp3_44100_128', {
    method:'POST',
    headers:{'xi-api-key':key,'Content-Type':'application/json'},
    body:JSON.stringify({text,model_id:model,language_code:'de',
                         voice_settings:settings})
  });
  if (!r.ok) throw Error(name + ': ElevenLabs ' + r.status + ': ' +
                         (await r.text()).slice(0,350));
  const data = await r.json();
  fs.writeFileSync(p, Buffer.from(data.audio_base64, 'base64'));
  fs.writeFileSync(j, JSON.stringify({text,voice,model,
    alignment:data.alignment,normalized_alignment:data.normalized_alignment},null,2));
  return {p, data:JSON.parse(fs.readFileSync(j, 'utf8'))};
}
const narrator = await speak('sprecher',voices.narrator,script,
  'eleven_multilingual_v2',
  {stability:.42,similarity_boost:.82,style:.38,use_speaker_boost:true,speed:1.08});
const brakk = await speak('brakk',voices.brakk,brakkText,'eleven_v3',
  {stability:.32,similarity_boost:.78,style:.85,use_speaker_boost:true,speed:1.08});
const zylla = await speak('zylla-gestaendnis',voices.zylla,zyllaText,'eleven_v3',
  {stability:.38,similarity_boost:.78,style:.72,use_speaker_boost:true,speed:1.00});

function alignment(data, needle) {
  for (const a of [data.alignment,data.normalized_alignment]) {
    if (a?.characters?.join('') === needle) return a;
  }
  throw Error('ElevenLabs alignment differs from text: ' + needle.slice(0,40));
}
function phraseWindow(data, phrase) {
  for (const a of [data.alignment,data.normalized_alignment]) {
    const i = a?.characters?.join('').indexOf(phrase) ?? -1;
    if (i >= 0) return {start:a.character_start_times_seconds[i],
      end:a.character_end_times_seconds[i + phrase.length - 1]};
  }
  throw Error('Character phrase absent from alignment: ' + phrase);
}
const A = alignment(narrator.data,script);
const B = phraseWindow(brakk.data,brakkText);
const Z = phraseWindow(zylla.data,zyllaWords);
const starts=[],ends=[]; let offset=0;
for (const line of lines) {
  starts.push(offset); offset += line.length; ends.push(offset-1); offset++;
}
const lead=.20;
const split = A.character_end_times_seconds[ends[3]] + .045;
const gapStart=lead+split;
const slamAt=gapStart+.35;
const brakkAt=slamAt+.12;
const afterAt=brakkAt+B.end+.06;
const zyllaAt=brakkAt+B.end+.53;
const zyllaVisibleAt=zyllaAt+Z.start;
const gap=zyllaAt+Z.end+.36-gapStart;
const narratorGapped=path.join(audio,'sprecher-mit-pause.wav');
const concat='[0:a]atrim=end=' + split +
  ',asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=mono[a0];' +
  '[1:a]atrim=duration=' + gap +
  ',asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=mono[s];' +
  '[0:a]atrim=start=' + split +
  ',asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=mono[a1];' +
  '[a0][s][a1]concat=n=3:v=0:a=1[a]';
run('ffmpeg',['-y','-loglevel','error','-i',narrator.p,
  '-f','lavfi','-t',String(gap),'-i','anullsrc=r=44100:cl=mono',
  '-filter_complex',concat,'-map','[a]','-c:a','pcm_s16le',narratorGapped]);
const startAt=i=>lead+A.character_start_times_seconds[i]+(i>ends[3]?gap:0);
const endAt=i=>lead+A.character_end_times_seconds[i]+(i>ends[3]?gap:0);
const lineStart=i=>startAt(starts[i]),lineEnd=i=>endAt(ends[i]);
const finalDuration=Math.max(lineEnd(6)+.55,zyllaAt+Z.end+.8);
if (finalDuration > 30.15)
  throw Error('Over 30 seconds: ' + finalDuration.toFixed(2) +
              '. Tighten speaker text and regenerate audio.');
const recorderAt=startAt(starts[3]+lines[3].indexOf('startet'))+.27;
const shieldAt=lineStart(6)+.43*(lineEnd(6)-lineStart(6));
const crossAt=lineStart(6)+.73*(lineEnd(6)-lineStart(6));
const events={
  scanner_at:Math.min(.95,lineEnd(0)*.31),
  intro_end:lineEnd(0)+.08,
  fatigue_at:lineStart(2),
  recorder_at:recorderAt,
  slam_at:slamAt,
  after_at:afterAt,
  zylla_at:zyllaVisibleAt,
  consent_at:lineStart(4),
  law1_at:lineStart(5),
  law1_reaction_at:lineStart(5)+Math.min(2.75,
    .55*(lineStart(6)-lineStart(5))),
  law2_at:lineStart(6),
  shield_at:shieldAt,
  cross_at:crossAt
};
for (const [n,t] of Object.entries(events))
  if (!(t>=0 && t<finalDuration)) throw Error('Bad time '+n+': '+t);
if (!(events.slam_at<events.after_at && events.after_at<events.zylla_at &&
      events.zylla_at<events.consent_at))
  throw Error('Action and dialogue order failed: '+JSON.stringify(events));

function stamp(t) {
  const c=Math.round(t*100);
  return Math.floor(c/360000)+':'+String(Math.floor(c/6000)%60).padStart(2,'0')+
    ':'+String(Math.floor(c/100)%60).padStart(2,'0')+'.'+
    String(c%100).padStart(2,'0');
}
let ass='[Script Info]\nTitle: Herr Jurist 30 September v7\nScriptType: v4.00+\n'+
  'PlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\nScaledBorderAndShadow: yes\n\n'+
  '[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, '+
  'SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, '+
  'StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, '+
  'Alignment, MarginL, MarginR, MarginV, Encoding\n'+
  'Style: Phrase,Nimbus Sans,72,&H00FAFAFA&,&H00FAFAFA&,&H00191919&,'+
  '&H90000000&,-1,0,0,0,100,100,0,0,1,2.5,2,2,110,170,280,1\n\n'+
  '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, '+
  'MarginV, Effect, Text\n';
function caption(start,end,display) {
  const size=display.length>25?55:display.length>18?64:72;
  ass+='Dialogue: 0,'+stamp(start)+','+stamp(Math.max(end,start+.13))+
    ',Phrase,,0,0,0,,{\\fs'+size+'\\fad(70,70)}'+display+'\n';
}
const phrases=[
  ['Sie unterschreibt.'],['Trotzdem ist ihr Geständnis'],['unverwertbar.'],['Warum?'],
  ['Zurück.'],['Brakk hält Zylla'],['die ganze Nacht wach.'],
  ['Sie nickt'],['immer wieder weg.'],['Er startet'],['die Aufnahme.'],
  ['Später willigt sie'],['in die Verwertung ein.'],
  ['Paragraf einhundertsechsunddreißig A','§ 136a'],
  ['verbietet Ermüdung'],['als Vernehmungsmethode.'],
  ['Absatz drei:','Abs. 3:'],['Auch ihre Einwilligung'],
  ['macht das Geständnis'],['nicht verwertbar.']
];
if (phrases.map(p=>p[0]).join(' ').replace(/\s/g,'') !== script.replace(/\s/g,''))
  throw Error('Captions do not cover the entire spoken narration');
const rows=[];let cursor=0;
for (const [spoken,shown=spoken] of phrases) {
  const first=script.indexOf(spoken,cursor);
  if (first<cursor) throw Error('Caption phrase missing: '+spoken);
  const last=first+spoken.length-1;
  rows.push({start:startAt(first),end:endAt(last)+.05,shown});
  cursor=last+1;
}
for (let i=0;i<rows.length;i++) {
  const p=rows[i];
  const next=rows[i+1] ? rows[i+1].start-.025 : Infinity;
  caption(p.start,Math.min(p.end,next),p.shown);
}
caption(brakkAt+B.start,brakkAt+B.end+.08,brakkText);
caption(zyllaAt+Z.start,zyllaAt+Z.end+.08,zyllaWords);
fs.writeFileSync(path.join(out,'untertitel-sinngruppen.ass'),ass);

const effects=[
  {name:'scanner',at:events.scanner_at,volume:.32,seconds:1.0,
   prompt:'One crisp futuristic tabletop scanner rejection: short red alert chirp, metallic click and electric stop. No words, music or screaming.'},
  {name:'rewind',at:events.intro_end+.03,volume:.22,seconds:.9,
   prompt:'Brief cinematic backwards tape and clock whoosh into a night interrogation, dry and punchy, no speech or music.'},
  {name:'room',at:events.intro_end+.5,volume:.05,seconds:5,
   prompt:'Low nocturnal interrogation-room atmosphere: soft fluorescent hum and distinct restrained clock ticks, no voices or music.'},
  {name:'recorder',at:events.recorder_at,volume:.22,seconds:.7,
   prompt:'A small digital voice recorder switching into record with a distinct mechanical click and short LED electronic beep, no words or music.'},
  {name:'table',at:slamAt,volume:.62,seconds:1.1,
   prompt:'One VERY loud, sharp, hard leather glove fist smashing against a STEEL interrogation table, high snap with deep body, brief metallic rattle, unmistakable physical hit, no voice or music.'},
  {name:'hologram',at:events.law1_at+.09,volume:.17,seconds:.75,
   prompt:'Short orange tabletop legal hologram appearing with a restrained sci-fi activation tone, no words or music.'},
  {name:'shield',at:shieldAt,volume:.35,seconds:1.2,
   prompt:'Recorded audio signal slams into a glowing protective energy shield, sharp electric crack, brief sparking tail, no voice or music.'},
  {name:'paper',at:crossAt,volume:.25,seconds:.8,
   prompt:'One sharp dry red rejection mark stamping the signed legal paper, short snap and paper thud, no speech or music.'}
];
for (const e of effects) {
  e.path=path.join(audio,e.name+'.mp3');
  if (fs.existsSync(e.path)) continue;
  const r=await fetch('https://api.elevenlabs.io/v1/sound-generation',{
    method:'POST',headers:{'xi-api-key':key,'Content-Type':'application/json'},
    body:JSON.stringify({text:e.prompt,duration_seconds:e.seconds,
      prompt_influence:.8,model_id:'eleven_text_to_sound_v2'})});
  if (!r.ok) throw Error(e.name+' SFX '+r.status+': '+
                         (await r.text()).slice(0,300));
  fs.writeFileSync(e.path,Buffer.from(await r.arrayBuffer()));
}
const timing={script,lines,lead,gap,events,final_duration:finalDuration,fps:30,
  voices,brakk_text:brakkText,zylla_text:zyllaWords,
  brakk_at:brakkAt,zylla_audio_at:zyllaAt,
  effects:effects.map(({path:unused,...effect})=>effect)};
fs.writeFileSync(path.join(out,'timing.json'),JSON.stringify(timing,null,2));
run('python3',[path.join(root,'make_frames.py'),'--timing',
  path.join(out,'timing.json'),'--out',path.join(out,'silent.mp4')]);
const ms=t=>Math.round(Math.max(0,t)*1000);
const filters=[
  '[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,volume=.83[narrator]',
  '[2:a]highpass=f=80,volume=.94,adelay='+ms(brakkAt)+':all=1[brakk]',
  // V3 delivered an intentionally weak performance at about -26 LUFS.
  // Lift the line so the words remain clear without undoing her exhaustion.
  '[3:a]highpass=f=110,volume=2.7,adelay='+ms(zyllaAt)+':all=1[zylla]'
];
effects.forEach((e,i)=>filters.push('['+(i+4)+':a]highpass=f=90,volume='+
  e.volume+',adelay='+ms(e.at)+':all=1[s'+i+']'));
filters.push('[narrator][brakk][zylla]'+effects.map((_,i)=>'[s'+i+']').join('')+
  'amix=inputs='+(effects.length+3)+
  ':duration=longest:normalize=0,alimiter=limit=0.94,apad[a]');
const dest=path.join(out,'herrjurist-2026-09-30-136a-v7-ruhiger-schnitt.mp4');
run('ffmpeg',['-y','-loglevel','error','-i',path.join(out,'silent.mp4'),
  '-i',narratorGapped,'-i',brakk.p,'-i',zylla.p,
  ...effects.flatMap(e=>['-i',e.path]),'-filter_complex',filters.join(';'),
  '-map','0:v:0','-map','[a]','-vf',
  'ass='+path.join(out,'untertitel-sinngruppen.ass'),
  '-c:v','libx264','-preset','medium','-crf','19','-pix_fmt','yuv420p',
  '-r','30','-c:a','aac','-b:a','192k','-ar','48000',
  '-t',String(finalDuration),'-movflags','+faststart',dest]);
if (fs.statSync(dest).size<1_000_000 ||
    Math.abs(duration(dest)-finalDuration)>.20)
  throw Error('Incomplete video export');
run('ffmpeg',['-y','-loglevel','error','-ss','1.2','-i',dest,
  '-frames:v','1','-q:v','3',path.join(out,'cover.jpg')]);
console.log(dest+': '+duration(dest).toFixed(2)+'s, 30fps, no zoom, voices '+
            JSON.stringify(voices));
