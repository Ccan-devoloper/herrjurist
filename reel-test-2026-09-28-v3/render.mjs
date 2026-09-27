import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root = path.resolve('reel-test-2026-09-28-v3');
const out = path.join(root, 'out');
fs.mkdirSync(out, { recursive: true });
// A single, causal case. Narration, cut points, on-screen law and effects use these beats.
const lines = [
  "Die Behörde sperrt Rex' Werkstatt.",
  'Rex zieht dagegen vor Gericht und reicht Klage ein.',
  'Doch kurz danach hebt die Behörde das Verbot wieder auf.',
  'Prozess vorbei? Nein: Nächste Woche soll dieselbe Sperre erneut kommen.',
  'Form-7 erklärt: Der Verwaltungsakt erledigt sich erst nach der Klageerhebung.',
  'Dann greift Paragraf eins dreizehn Absatz eins Satz vier VwGO.',
  'Die konkrete Wiederholungsgefahr kann Rex das nötige Feststellungsinteresse geben.',
  'Merke: Erst den Erledigungszeitpunkt, dann das Interesse, dann Rechtswidrigkeit und Rechtsverletzung prüfen.'
];
const script=lines.join(' ');
const key=process.env.ELEVENLABS_API_KEY;
if (!key && !process.env.REEL_VOICE_PATH) throw new Error('ElevenLabs-Schlüssel fehlt');
const voice=process.env.ELEVENLABS_VOICE_ID || 'PhufIH7nYh2Up1uej6aY';
const model=process.env.ELEVENLABS_MODEL || 'eleven_multilingual_v2';
const run=(cmd,args)=>{const r=spawnSync(cmd,args,{encoding:'utf8',stdio:['ignore','pipe','pipe']});if(r.status!==0)throw new Error(`${cmd}: ${r.stderr.slice(-2500)}`);return r.stdout.trim()};
const duration=p=>Number(run('ffprobe',['-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',p]));
let voicePath=process.env.REEL_VOICE_PATH;
let alignment;
if(!voicePath){
  const response=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${encodeURIComponent(voice)}/with-timestamps?output_format=mp3_44100_128`,{
    method:'POST',headers:{'xi-api-key':key,'Content-Type':'application/json'},
    body:JSON.stringify({text:script,model_id:model,language_code:'de',voice_settings:{stability:.38,similarity_boost:.8,style:.42,use_speaker_boost:true,speed:1.03}})
  });
  if(!response.ok)throw new Error(`TTS ${response.status}: ${(await response.text()).slice(0,300)}`);
  const spoken=await response.json();
  voicePath=path.join(out,'sprecher-elevenlabs.mp3');
  fs.writeFileSync(voicePath,Buffer.from(spoken.audio_base64,'base64'));
  alignment=spoken.alignment?.character_end_times_seconds || spoken.normalized_alignment?.character_end_times_seconds;
}
const voiceDuration=duration(voicePath), lead=.36, fps=30;
let chars=0;
const b=[0];
for(const line of lines){chars+=line.length;b.push((alignment?.[chars-1]??voiceDuration*chars/script.length)+lead);chars++}
b[b.length-1]=voiceDuration+lead+.2;
const I=n=>`${String(n).padStart(2,'0')}.jpg`;
const beats=[
  {at:0,until:b[1],image:I(1),event:'official-lock'},
  {at:b[1],until:b[1]+(b[2]-b[1])*.37,image:I(2)},
  {at:b[1]+(b[2]-b[1])*.37,until:b[1]+(b[2]-b[1])*.69,image:I(3)},
  {at:b[1]+(b[2]-b[1])*.69,until:b[2],image:I(4),event:'filing-stamp',punch:1.06},
  {at:b[2],until:b[3],image:I(5),event:'unlock'},
  {at:b[3],until:b[3]+(b[4]-b[3])*.58,image:I(6),event:'recurrence'},
  {at:b[3]+(b[4]-b[3])*.58,until:b[4],image:I(7),punch:1.04},
  {at:b[4],until:b[5],image:I(8)},
  {at:b[5],until:b[6],image:I(8),punch:1.06,style:'law'},
  {at:b[6],until:b[7],image:I(7)},
  {at:b[7],until:b[8],image:I(9),style:'takeaway'}
];
if(beats.some(x=>x.until-x.at<.22))throw new Error('Voice-/Szenengrenzen: '+JSON.stringify(b));
const font=path.resolve('fonts/Anton.ttf'),fontBody=path.resolve('fonts/SpaceGrotesk.ttf');
for(let i=0;i<beats.length;i++){
  const x=beats[i],input=path.join(root,'shots',x.image),output=path.join(out,`scene-${String(i+1).padStart(2,'0')}.mp4`);
  const z=x.punch||1,w=Math.round(1080*z/2)*2,h=Math.round(1920*z/2)*2;
  let vf=`scale=${w}:${h}:force_original_aspect_ratio=increase,crop=1080:1920:(iw-1080)/2:(ih-1920)/2,format=yuv420p`;
  // Exact typography sits inside Form-7's already illustrated in-world holograms.
  if(x.style==='law')vf+=`,drawtext=fontfile=${font}:text='§ 113 I 4':fontsize=56:fontcolor=white:shadowcolor=0x003f29:shadowx=2:shadowy=2:x=575:y=505,drawtext=fontfile=${font}:text='VwGO':fontsize=55:fontcolor=white:shadowcolor=0x003f29:shadowx=2:shadowy=2:x=575:y=580,drawtext=fontfile=${fontBody}:text='KLAGE → ERLEDIGUNG':fontsize=31:fontcolor=0xc6ffe4:x=555:y=675`;
  if(x.style==='takeaway')vf+=`,drawtext=fontfile=${font}:text='MERKE':fontsize=61:fontcolor=white:shadowcolor=0x003f29:shadowx=2:shadowy=3:x=685:y=705,drawtext=fontfile=${fontBody}:text='1  ZEITPUNKT':fontsize=35:fontcolor=white:x=585:y=800,drawtext=fontfile=${fontBody}:text='2  INTERESSE':fontsize=35:fontcolor=white:x=585:y=865,drawtext=fontfile=${fontBody}:text='3  RECHTSWIDRIGKEIT':fontsize=30:fontcolor=white:x=585:y=930,drawtext=fontfile=${fontBody}:text='+ RECHTSVERLETZUNG':fontsize=27:fontcolor=white:x=585:y=990`;
  run('ffmpeg',['-y','-loglevel','error','-loop','1','-framerate',String(fps),'-i',input,'-vf',vf,'-frames:v',String(Math.round((x.until-x.at)*fps)),'-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-an',output]);
  x.output=output;
}
let actualAt=0;
for(const x of beats){x.actualAt=actualAt;actualAt+=duration(x.output)}
fs.writeFileSync(path.join(out,'concat.txt'),beats.map(x=>`file '${x.output}'`).join('\n')+'\n');
const silent=path.join(out,'silent.mp4');
run('ffmpeg',['-y','-loglevel','error','-f','concat','-safe','0','-i',path.join(out,'concat.txt'),'-c','copy',silent]);
async function sfx(name,prompt,seconds){
  const r=await fetch('https://api.elevenlabs.io/v1/sound-generation',{method:'POST',headers:{'xi-api-key':key,'Content-Type':'application/json'},body:JSON.stringify({text:prompt,duration_seconds:seconds,prompt_influence:.75,model_id:'eleven_text_to_sound_v2'})});
  if(!r.ok)throw new Error(`SFX ${name}: ${r.status} ${(await r.text()).slice(0,200)}`);
  const p=path.join(out,`${name}-elevenlabs.mp3`);fs.writeFileSync(p,Buffer.from(await r.arrayBuffer()));return p;
}
const events=[
  {name:'lock',prompt:'A forceful futuristic municipal metal workshop security door lock slams shut, crisp heavy steel CLANG with short electrical seal buzz, strong attack, no voices, no music.',seconds:1.4,event:'official-lock',offset:.5,volume:.42},
  {name:'stamp',prompt:'Single decisive courthouse paper filing rubber stamp WHACK sharply onto a document on wooden counter, tactile crisp impact, no voices, no music.',seconds:.9,event:'filing-stamp',offset:.12,volume:.5},
  {name:'unlock',prompt:'Heavy industrial workshop rolling shutter unlocks with metallic latch CLACK and short servo rise, then door starts lifting. No voice, no music.',seconds:1.4,event:'unlock',offset:.12,volume:.35},
  {name:'alert',prompt:'One dramatic crisp electronic warning chirp followed by a quick tense low pulse as an official future ban notification appears on a tablet, no voice, no music.',seconds:1.0,event:'recurrence',offset:.25,volume:.28}
];
const tracks=[];
for(const e of events)tracks.push(await sfx(e.name,e.prompt,e.seconds));
const ms=t=>Math.max(0,Math.round(t*1000));
const filters=[`[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,adelay=${ms(lead)}:all=1,volume=0.82[v]`];
for(let i=0;i<events.length;i++){
  const e=events[i],time=beats.find(x=>x.event===e.event).actualAt+e.offset;
  e.actualAt=time;
  filters.push(`[${i+2}:a]highpass=f=95,volume=${e.volume},adelay=${ms(time)}:all=1[s${i}]`);
}
filters.push(`[v]${events.map((_,i)=>`[s${i}]`).join('')}amix=inputs=${events.length+1}:duration=longest:normalize=0,alimiter=limit=0.9[a]`);
const dest=path.join(out,'herrjurist-2026-09-28-story-prueffassung.mp4');
run('ffmpeg',['-y','-loglevel','error','-i',silent,'-i',voicePath,...tracks.flatMap(p=>['-i',p]),'-filter_complex',filters.join(';'),'-map','0:v:0','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-t',String(b[8]),'-movflags','+faststart',dest]);
if(fs.statSync(dest).size<1000000||duration(dest)<b[8]-.2)throw new Error('MP4 unvollständig');
fs.writeFileSync(path.join(out,'timing.json'),JSON.stringify({script,voice,model,voiceDuration,lead,boundaries:b,events,beats:beats.map(x=>({at:x.at,actualAt:x.actualAt,until:x.until,image:x.image,punch:x.punch||1,style:x.style||null}))},null,2));
console.log(`${dest}; ${duration(dest).toFixed(2)}s`);
