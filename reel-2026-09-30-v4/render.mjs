import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';

const root=path.resolve('reel-2026-09-30-v4');
const out=path.join(root,'out'),audio=path.join(root,'audio');
for(const p of [out,audio])fs.mkdirSync(p,{recursive:true});
const key=process.env.ELEVENLABS_API_KEY;
const VOICES={narrator:'PhufIH7nYh2Up1uej6aY',brakk:'JiW03c2Gt43XNUQAumRP',zylla:'xLCJR8xcZX2YjImGFyGw'};
if(!key)throw Error('ELEVENLABS_API_KEY fehlt');
const lines=[
  'Unterschrieben. Trotzdem gesperrt. Warum?',
  'Zurück. Brakk hält Zylla die ganze Nacht wach.',
  'Stunde um Stunde. Sie sackt weg.',
  'Erschöpft spricht sie. Das Gerät nimmt auf.',
  'Paragraf einhundertsechsunddreißig A verbietet Ermüdung als Vernehmungsmethode.',
  'Absatz drei: Ihre Einwilligung rettet die Aussage nicht.',
  'Die Unterschrift heilt den Verstoß nicht.'
];
const script=lines.join(' '),brakkText='Jetzt rede!',zyllaText='[sighing wearily] Haa...';
const run=(cmd,args)=>{
  const r=spawnSync(cmd,args,{encoding:'utf8',stdio:['ignore','pipe','pipe'],maxBuffer:64*1024*1024});
  if(r.status!==0)throw Error(`${cmd}: ${r.stderr.slice(-4500)}`);
  return r.stdout.trim();
};
const dur=p=>Number(run('ffprobe',['-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',p]));
async function speak(name,voice,text,model,settings){
  const p=path.join(audio,`${name}.mp3`),a=path.join(audio,`${name}.json`);
  if(fs.existsSync(p)&&fs.existsSync(a))return {p,data:JSON.parse(fs.readFileSync(a))};
  const response=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voice}/with-timestamps?output_format=mp3_44100_128`,{
    method:'POST',headers:{'xi-api-key':key,'Content-Type':'application/json'},
    body:JSON.stringify({text,model_id:model,language_code:'de',
      voice_settings:settings})
  });
  if(!response.ok)throw Error(`${name}: ElevenLabs ${response.status}: ${(await response.text()).slice(0,350)}`);
  const data=await response.json();
  fs.writeFileSync(p,Buffer.from(data.audio_base64,'base64'));
  fs.writeFileSync(a,JSON.stringify({text,voice,model,alignment:data.alignment,normalized_alignment:data.normalized_alignment},null,2));
  return {p,data:JSON.parse(fs.readFileSync(a))};
}
const narrator=await speak('sprecher',VOICES.narrator,script,'eleven_multilingual_v2',
  {stability:.42,similarity_boost:.82,style:.38,use_speaker_boost:true,speed:1.09});
const brakk=await speak('brakk',VOICES.brakk,brakkText,'eleven_v3',
  {stability:.32,similarity_boost:.78,style:.88,use_speaker_boost:true,speed:1.12});
const zylla=await speak('zylla-seufzer',VOICES.zylla,zyllaText,'eleven_v3',
  {stability:.35,similarity_boost:.72,style:.62,use_speaker_boost:true});

const A=[narrator.data.alignment,narrator.data.normalized_alignment].find(x=>x?.characters?.join('')===script);
if(!A)throw Error('Erzähler-Alignment weicht vom Skript ab.');
const B=[brakk.data.alignment,brakk.data.normalized_alignment].find(x=>x?.characters?.join('')===brakkText);
if(!B)throw Error('Brakk-Alignment weicht vom gesprochenen Text ab.');
const lead=.20,brakkDuration=dur(brakk.p),zyllaDuration=dur(zylla.p);
const gap=brakkDuration+.32;
const ends=[],starts=[];let pos=0;
for(const line of lines){starts.push(pos);pos+=line.length;ends.push(pos-1);pos++;}
const splitAt=A.character_end_times_seconds[ends[2]]+.045;
const narratorGapped=path.join(audio,'sprecher-mit-pause.wav');
run('ffmpeg',['-y','-loglevel','error','-i',narrator.p,
  '-f','lavfi','-t',String(gap),'-i','anullsrc=r=44100:cl=mono',
  '-filter_complex',`[0:a]atrim=end=${splitAt},asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=mono[a0];[1:a]atrim=duration=${gap},asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=mono[s];[0:a]atrim=start=${splitAt},asetpts=PTS-STARTPTS,aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=mono[a1];[a0][s][a1]concat=n=3:v=0:a=1[a]`,
  '-map','[a]','-c:a','pcm_s16le',narratorGapped]);
const startAt=i=>lead+A.character_start_times_seconds[i]+(i>ends[2]?gap:0);
const endAt=i=>lead+A.character_end_times_seconds[i]+(i>ends[2]?gap:0);
const boundaries=[0,...ends.map((idx,i)=>endAt(idx)+.02)];
const characterStart=lead+splitAt+.12;
const tableAt=characterStart+B.character_start_times_seconds[brakkText.indexOf('rede!')]+.12;
const sighAt=Math.max(boundaries[2]+.6,boundaries[3]-Math.min(zyllaDuration+.10,1.25));
const finalDuration=Math.max(29.25,dur(narratorGapped)+lead+.45);
boundaries[boundaries.length-1]=finalDuration;
const scannerAt=Math.min(1.45,boundaries[1]*.45);
const shieldAt=boundaries[5]+Math.min(2,.49*(boundaries[6]-boundaries[5]));
const crossAt=boundaries[6]+Math.min(1.10,.36*(finalDuration-boundaries[6]));

const stamp=t=>{const c=Math.round(t*100);return `${Math.floor(c/360000)}:${String(Math.floor(c/6000)%60).padStart(2,'0')}:${String(Math.floor(c/100)%60).padStart(2,'0')}.${String(c%100).padStart(2,'0')}`;};
let ass=`[Script Info]\nTitle: Herr Jurist 30 September cartoon reel\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\nScaledBorderAndShadow: yes\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Word,Nimbus Sans,72,&H00FAFAFA&,&H00FAFAFA&,&H00191919&,&H90000000&,-1,0,0,0,100,100,0,0,1,2.5,2,2,110,170,280,1\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n`;
const add=(start,stop,display)=>{
  if(stop<start)throw Error(`Caption rückwärts: ${display}`);
  const size=display.length>21?55:display.length>16?64:72;
  ass+=`Dialogue: 0,${stamp(start)},${stamp(Math.max(stop,start+.11))},Word,,0,0,0,,{\\fs${size}\\fad(35,40)\\fscx106\\fscy106\\t(0,110,\\fscx100\\fscy100)}${display}\n`;
};
const words=[...script.matchAll(/\S+/g)];
for(let i=0;i<words.length;i++){
  const m=words[i];let display=m[0],last=m.index+display.length-1;
  if(display==='Paragraf'&&words[i+1]?.[0]==='einhundertsechsunddreißig'&&words[i+2]?.[0]==='A'){
    display='§ 136a';last=words[i+2].index;i+=2;
  }else if(display==='Absatz'&&words[i+1]?.[0]==='drei:'){
    display='Abs. 3:';last=words[i+1].index+words[i+1][0].length-1;i++;
  }
  add(startAt(m.index),endAt(last),display);
}
// A short meaningful character sentence is captioned in the same quiet style.
add(characterStart+B.character_start_times_seconds[0],characterStart+B.character_end_times_seconds[4],'Jetzt');
add(characterStart+B.character_start_times_seconds[6],characterStart+B.character_end_times_seconds[10],'rede!');
fs.writeFileSync(path.join(out,'untertitel-einzelwort.ass'),ass);

const effects=[
  {name:'scanner',at:scannerAt,volume:.32,seconds:1.0,prompt:'One crisp futuristic tabletop scanner rejection: short red alert chirp, metallic click and electric stop. No words, music or screaming.'},
  {name:'rewind',at:boundaries[1]+.03,volume:.22,seconds:.9,prompt:'Brief cinematic backwards tape and clock whoosh into a night interrogation, dry and punchy, no speech or music.'},
  {name:'room',at:boundaries[1]+.7,volume:.06,seconds:5,prompt:'Low nocturnal interrogation-room atmosphere: soft fluorescent hum and distinct restrained clock ticks, no voices or music.'},
  {name:'table',at:tableAt,volume:.55,seconds:1.1,prompt:'One VERY loud, sharp, hard leather glove fist smashing against a STEEL interrogation table, high snap with deep body, brief metallic rattle, unmistakable physical hit, no voice or music.'},
  {name:'recorder',at:boundaries[3]+gap+.75,volume:.18,seconds:.7,prompt:'A small digital voice recorder switching into record with a distinct mechanical click and short LED electronic beep, no words or music.'},
  {name:'hologram',at:boundaries[4]+.08,volume:.18,seconds:.75,prompt:'Short orange tabletop legal hologram appearing with a restrained sci-fi activation tone, no words or music.'},
  {name:'shield',at:shieldAt,volume:.36,seconds:1.2,prompt:'Recorded audio signal slams into a glowing protective energy shield, sharp electric crack, brief sparking tail, no voice or music.'},
  {name:'paper',at:crossAt,volume:.26,seconds:.8,prompt:'One sharp dry red rejection mark stamping the signed legal paper, short snap and paper thud, no speech or music.'}
];
// The recorder click belongs to the second half of the statement line.
effects[4].at=boundaries[3]+.70*(boundaries[4]-boundaries[3]);
for(const e of effects){
  e.path=path.join(audio,`${e.name}.mp3`);
  if(fs.existsSync(e.path))continue;
  const r=await fetch('https://api.elevenlabs.io/v1/sound-generation',{method:'POST',
    headers:{'xi-api-key':key,'Content-Type':'application/json'},
    body:JSON.stringify({text:e.prompt,duration_seconds:e.seconds,prompt_influence:.8,model_id:'eleven_text_to_sound_v2'})});
  if(!r.ok)throw Error(`${e.name} SFX ${r.status}: ${(await r.text()).slice(0,300)}`);
  fs.writeFileSync(e.path,Buffer.from(await r.arrayBuffer()));
}
const T={script,lines,boundaries,lead,gap,character_start:characterStart,character_end:characterStart+brakkDuration,
  sigh_at:sighAt,table_at:tableAt,scanner_at:scannerAt,shield_at:shieldAt,cross_at:crossAt,
  final_duration:finalDuration,fps:30,voices:VOICES,
  effects:effects.map(({path:_,...e})=>e)};
fs.writeFileSync(path.join(out,'timing.json'),JSON.stringify(T,null,2));
run('python3',[path.join(root,'make_frames.py'),'--timing',path.join(out,'timing.json'),'--out',path.join(out,'silent.mp4')]);
const ms=t=>Math.round(Math.max(0,t)*1000);
const filters=[
  '[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,volume=.82[narrator]',
  `[2:a]highpass=f=80,volume=.92,adelay=${ms(characterStart)}:all=1[brakk]`,
  `[3:a]highpass=f=110,volume=.39,adelay=${ms(sighAt)}:all=1[zylla]`
];
effects.forEach((e,i)=>filters.push(`[${i+4}:a]highpass=f=90,volume=${e.volume},adelay=${ms(e.at)}:all=1[s${i}]`));
filters.push(`[narrator][brakk][zylla]${effects.map((_,i)=>`[s${i}]`).join('')}amix=inputs=${effects.length+3}:duration=longest:normalize=0,alimiter=limit=0.92,apad[a]`);
const dest=path.join(out,'herrjurist-2026-09-30-136a-cartoon-prueffassung.mp4');
run('ffmpeg',['-y','-loglevel','error','-i',path.join(out,'silent.mp4'),'-i',narratorGapped,'-i',brakk.p,'-i',zylla.p,
  ...effects.flatMap(e=>['-i',e.path]),'-filter_complex',filters.join(';'),
  '-map','0:v:0','-map','[a]','-vf',`ass=${path.join(out,'untertitel-einzelwort.ass')}`,
  '-c:v','libx264','-preset','medium','-crf','19','-pix_fmt','yuv420p','-r','30',
  '-c:a','aac','-b:a','192k','-ar','48000','-t',String(finalDuration),'-movflags','+faststart',dest]);
if(fs.statSync(dest).size<1_000_000||Math.abs(dur(dest)-finalDuration)>.2)throw Error('Export unvollständig.');
run('ffmpeg',['-y','-loglevel','error','-ss','.8','-i',dest,'-frames:v','1','-q:v','3',path.join(out,'cover.jpg')]);
console.log(`${dest}: ${dur(dest).toFixed(2)}s, 30fps, cartoon keyframes, voices ${JSON.stringify(VOICES)}`);
