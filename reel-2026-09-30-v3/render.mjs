import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root=path.resolve('reel-2026-09-30-v3');
const out=path.join(root,'out'), audio=path.join(root,'audio');
for(const p of [out,audio])fs.mkdirSync(p,{recursive:true});
const key=process.env.ELEVENLABS_API_KEY;
const voice=process.env.ELEVENLABS_VOICE_ID||'PhufIH7nYh2Up1uej6aY';
const model='eleven_multilingual_v2';
const lines=[
  'Zylla willigt ein. Trotzdem: Aussage gesperrt. Warum?',
  'Zurück in die Nacht. Brakk hält sie absichtlich wach.',
  'Stunde um Stunde. Zylla sackt weg. Er fragt weiter.',
  'Erst völlig erschöpft spricht sie. Die Aufnahme läuft.',
  'Paragraf einhundertsechsunddreißig A der StPO verbietet Ermüdung als Vernehmungsmethode.',
  'Absatz drei: Selbst ihre Einwilligung rettet die Aussage nicht.',
  'Die Unterschrift heilt den Verstoß nicht.'
];
const script=lines.join(' ');
const run=(cmd,args)=>{
  const r=spawnSync(cmd,args,{encoding:'utf8',stdio:['ignore','pipe','pipe'],maxBuffer:40*1024*1024});
  if(r.status!==0)throw Error(`${cmd}: ${r.stderr.slice(-5000)}`);
  return r.stdout.trim();
};
const dur=p=>Number(run('ffprobe',['-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',p]));
const voicePath=path.join(audio,'sprecher.mp3');
const alignPath=path.join(audio,'alignment.json');
if(!fs.existsSync(voicePath)||!fs.existsSync(alignPath)){
  if(!key)throw Error('ELEVENLABS_API_KEY fehlt für eine neue Aufnahme.');
  const r=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voice}/with-timestamps?output_format=mp3_44100_128`,{
    method:'POST',headers:{'xi-api-key':key,'Content-Type':'application/json'},
    body:JSON.stringify({text:script,model_id:model,language_code:'de',voice_settings:{
      stability:.40,similarity_boost:.82,style:.38,use_speaker_boost:true,speed:1.065}})
  });
  if(!r.ok)throw Error(`ElevenLabs Sprecher ${r.status}: ${(await r.text()).slice(0,400)}`);
  const data=await r.json();
  fs.writeFileSync(voicePath,Buffer.from(data.audio_base64,'base64'));
  fs.writeFileSync(alignPath,JSON.stringify({script,alignment:data.alignment,normalized_alignment:data.normalized_alignment},null,2));
}
const raw=JSON.parse(fs.readFileSync(alignPath));
if(raw.script!==script)throw Error('Sprecher und Text stimmen nicht überein.');
const a=[raw.alignment,raw.normalized_alignment].find(x=>x?.characters?.join('')===script);
if(!a)throw Error('ElevenLabs hat kein zeichengetreues Alignment geliefert.');
const lead=.28,voiceDuration=dur(voicePath);
const cs=i=>(a.character_start_times_seconds[i]??voiceDuration*i/script.length)+lead;
const ce=i=>(a.character_end_times_seconds[i]??voiceDuration*(i+1)/script.length)+lead;
const boundaries=[0];let pos=0;
for(const line of lines){pos+=line.length;boundaries.push(ce(pos-1)+.025);pos++;}
const finalDuration=Math.max(voiceDuration+lead+.45,boundaries.at(-1)+.25);
boundaries[boundaries.length-1]=finalDuration;
const stamp=t=>{let c=Math.round(t*100);return `${Math.floor(c/360000)}:${String(Math.floor(c/6000)%60).padStart(2,'0')}:${String(Math.floor(c/100)%60).padStart(2,'0')}.${String(c%100).padStart(2,'0')}`;};
let ass=`[Script Info]\nTitle: Herr Jurist 30.09 §136a limited animation\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\nScaledBorderAndShadow: yes\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Word,Nimbus Sans,72,&H00FAFAFA&,&H00FAFAFA&,&H00191919&,&H90000000&,-1,0,0,0,100,100,0,0,1,2.5,2,2,110,170,280,1\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n`;
let cues=0;const words=[...script.matchAll(/\S+/g)];
for(let i=0;i<words.length;i++){
  const m=words[i];let display=m[0],end=m.index+m[0].length-1;
  if(display==='Paragraf'&&words[i+1]?.[0]==='einhundertsechsunddreißig'&&words[i+2]?.[0]==='A'){
    display='§ 136a';end=words[i+2].index;i+=2;
  }else if(display==='Absatz'&&words[i+1]?.[0]==='drei:'){
    display='Abs. 3:';end=words[i+1].index+words[i+1][0].length-1;i++;
  }
  const start=cs(m.index),stop=Math.max(ce(end),start+.12);
  const fontsize=display.length>22?62:72;
  ass+=`Dialogue: 0,${stamp(start)},${stamp(stop)},Word,,0,0,0,,{\\fs${fontsize}\\fad(35,40)\\fscx106\\fscy106\\t(0,110,\\fscx100\\fscy100)}${display}\n`;
  cues++;
}
fs.writeFileSync(path.join(out,'untertitel-einzelwort.ass'),ass);
const effects=[
  {name:'deny',at:boundaries[0]+(boundaries[1]-boundaries[0])*.51,volume:.29,seconds:1.1,
   prompt:'One sharp futuristic desk evidence scanner rejecting a signed document: clean bright electrical buzz, quick metallic clack, short red alarm decay, no words, music or scream.'},
  {name:'rewind',at:boundaries[1]+.08,volume:.18,seconds:1.0,
   prompt:'Very short cinematic backwards tape and reversed mechanical clock whoosh into a late-night interrogation flashback, dry and punchy, no words or music.'},
  {name:'room',at:boundaries[1]+.6,volume:.075,seconds:4.0,
   prompt:'Quiet tense nocturnal interrogation-room ambience with subtle mechanical clock ticks and fluorescent electric hum, background only, no voices, no music.'},
  {name:'table',at:boundaries[3]+(boundaries[4]-boundaries[3])*.12,volume:.48,seconds:1.1,
   prompt:'A heavy leather-gloved fist strikes a steel interrogation table once, loud sharp bright metallic CRACK with deep weight and a short table rattle, clear immediate attack, no voice, music or scream.'},
  {name:'record',at:boundaries[3]+(boundaries[4]-boundaries[3])*.45,volume:.13,seconds:1.0,
   prompt:'Small recording device switches on with one short mechanical click and soft electronic tone, no voices or music.'},
  {name:'shield',at:boundaries[5]+(boundaries[6]-boundaries[5])*.52,volume:.33,seconds:1.4,
   prompt:'Recorded audio waveform crashes against a luminous legal force shield: strong sharp high-tech energy impact, crackling bright sparks then abrupt stop, no speech or music.'},
  {name:'paper',at:boundaries[6]+(boundaries[7]-boundaries[6])*.43,volume:.20,seconds:.9,
   prompt:'One sharp cinematic legal rejection mark striking a paper document on a steel desk, bright dry stamp smack with very short electronic spark, no words or music.'}
];
for(const e of effects){
  e.path=path.join(audio,`${e.name}.mp3`);
  if(fs.existsSync(e.path))continue;
  if(!key)throw Error(`ElevenLabs-SFX ${e.name} fehlt.`);
  const r=await fetch('https://api.elevenlabs.io/v1/sound-generation',{method:'POST',
    headers:{'xi-api-key':key,'Content-Type':'application/json'},
    body:JSON.stringify({text:e.prompt,duration_seconds:e.seconds,prompt_influence:.8,model_id:'eleven_text_to_sound_v2'})});
  if(!r.ok)throw Error(`ElevenLabs SFX ${e.name} ${r.status}: ${(await r.text()).slice(0,300)}`);
  fs.writeFileSync(e.path,Buffer.from(await r.arrayBuffer()));
}
const timing={script,lines,boundaries,finalDuration,voiceDuration,lead,fps:30,captionCues:cues,
  effects:effects.map(({path:_,...x})=>x),strategy:'locked master shots; regional blink, mouth, clock, fist, barrier animation; deliberate impact cuts'};
fs.writeFileSync(path.join(out,'timing.json'),JSON.stringify(timing,null,2));
run('python3',[path.join(root,'make_frames.py'),'--timing',path.join(out,'timing.json'),'--out',path.join(out,'silent.mp4')]);
const ms=t=>Math.round(Math.max(0,t)*1000);
const filters=[`[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,adelay=${ms(lead)}:all=1,volume=.85[v]`];
effects.forEach((e,i)=>filters.push(`[${i+2}:a]highpass=f=95,volume=${e.volume},adelay=${ms(e.at)}:all=1[s${i}]`));
filters.push(`[v]${effects.map((_,i)=>`[s${i}]`).join('')}amix=inputs=${effects.length+1}:duration=longest:normalize=0,alimiter=limit=0.92,apad[a]`);
const dest=path.join(out,'herrjurist-2026-09-30-136a-neu-prueffassung.mp4');
run('ffmpeg',['-y','-loglevel','error','-i',path.join(out,'silent.mp4'),'-i',voicePath,
  ...effects.flatMap(e=>['-i',e.path]),'-filter_complex',filters.join(';'),
  '-map','0:v:0','-map','[a]','-vf',`ass=${path.join(out,'untertitel-einzelwort.ass')}`,
  '-c:v','libx264','-preset','medium','-crf','19','-pix_fmt','yuv420p','-r','30',
  '-c:a','aac','-b:a','192k','-ar','48000','-t',String(finalDuration),'-movflags','+faststart',dest]);
if(fs.statSync(dest).size<1_000_000||Math.abs(dur(dest)-finalDuration)>.15)throw Error('Export unvollständig.');
run('ffmpeg',['-y','-loglevel','error','-ss','.8','-i',dest,'-frames:v','1','-q:v','3',path.join(out,'cover.jpg')]);
console.log(`${dest} ${dur(dest).toFixed(2)}s; 30 fps; ${cues} narrator captions`);
