import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const dir = path.resolve('reel-test-2026-09-28');
const out = path.join(dir, 'out');
fs.mkdirSync(out, { recursive: true });
const lines = [
  'Rex klagt gegen ein Platzverbot.',
  'Plötzlich hebt die Behörde es auf. Prozess vorbei?',
  'Form-7 sagt: Nicht so schnell. Entscheidend ist, wann der Verwaltungsakt verschwand.',
  'Nach Klageerhebung: Paragraf eins dreizehn Absatz eins Satz vier VwGO direkt. Schon vorher: entsprechend.',
  'Und Rex braucht ein besonderes Feststellungsinteresse, etwa konkrete Wiederholungsgefahr.',
  'Merke: Erledigungszeitpunkt, Interesse, dann Rechtswidrigkeit und Rechtsverletzung prüfen.'
];
const script = lines.join(' ');
const key = process.env.ELEVENLABS_API_KEY;
if (!key && !process.env.REEL_VOICE_PATH) throw new Error('ElevenLabs-Schlüssel fehlt.');
const voice = process.env.ELEVENLABS_VOICE_ID || 'PhufIH7nYh2Up1uej6aY';
const model = process.env.ELEVENLABS_MODEL || 'eleven_multilingual_v2';
const run = (command,args) => { const r=spawnSync(command,args,{encoding:'utf8',stdio:['ignore','pipe','pipe']}); if(r.status!==0) throw new Error(`${command}: ${r.stderr.slice(-2500)}`); return r.stdout.trim(); };
const duration = p => Number(run('ffprobe',['-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',p]));
let voicePath=process.env.REEL_VOICE_PATH;
let alignment;
if (!voicePath) {
  const response=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${encodeURIComponent(voice)}/with-timestamps?output_format=mp3_44100_128`,{
    method:'POST',headers:{'xi-api-key':key,'Content-Type':'application/json'},
    body:JSON.stringify({text:script,model_id:model,language_code:'de',voice_settings:{stability:.42,similarity_boost:.8,style:.36,use_speaker_boost:true,speed:1.06}})
  });
  if(!response.ok) throw new Error(`TTS ${response.status}: ${(await response.text()).slice(0,300)}`);
  const spoken=await response.json();
  voicePath=path.join(out,'sprecher-elevenlabs.mp3');
  fs.writeFileSync(voicePath,Buffer.from(spoken.audio_base64,'base64'));
  alignment=spoken.alignment?.character_end_times_seconds || spoken.normalized_alignment?.character_end_times_seconds;
}
const voiceDuration=duration(voicePath);
const lead=.48;
let chars=0;
const boundaries=[0];
for (const line of lines) {
  chars+=line.length;
  boundaries.push((alignment?.[chars-1] ?? voiceDuration*chars/script.length)+lead);
  chars++;
}
boundaries[boundaries.length-1]=voiceDuration+lead+.18;
const b=boundaries;
const fps=30;
const beats=[
  {at:0,until:.33,image:'01-ban.jpg'},
  {at:.33,until:b[1],image:'01-ban.jpg',punch:1.12,style:'hook'},
  {at:b[1],until:b[1]+2/fps,image:'02-shatter.jpg',punch:1.13},
  {at:b[1]+2/fps,until:b[1]+.73,image:'02-shatter.jpg'},
  {at:b[1]+.73,until:b[2],image:'03-after.jpg'},
  {at:b[2],until:b[3],image:'03-after.jpg',punch:1.10},
  {at:b[3],until:b[4]-.8,image:'04-timing.jpg',style:'norm'},
  {at:b[4]-.8,until:b[4],image:'04-timing.jpg',punch:1.10},
  {at:b[4],until:b[5],image:'05-court.jpg'},
  {at:b[5],until:b[6],image:'06-merke.jpg',style:'merke'}
];
if (beats.some(x=>x.until-x.at<1/fps)) throw new Error('Ungültige Voice-/Szenengrenze: '+JSON.stringify(b));
const font=path.resolve('fonts/Anton.ttf');
const fontHud=path.resolve('fonts/SpaceGrotesk.ttf');
for (let i=0;i<beats.length;i++) {
  const beat=beats[i],input=path.join(dir,'shots',beat.image),output=path.join(out,`scene-${String(i+1).padStart(2,'0')}.mp4`);
  const punch=beat.punch||1,w=Math.round(1080*punch/2)*2,h=Math.round(1920*punch/2)*2;
  const crop=`scale=${w}:${h}:force_original_aspect_ratio=increase,crop=1080:1920:(iw-1080)/2:(ih-1920)/2,format=yuv420p`;
  let filter=crop;
  if(beat.style==='hook') filter+=`,drawtext=fontfile=${font}:text='VERBOT WEG. KLAGE WEG?':fontsize=75:fontcolor=white:borderw=4:bordercolor=0x813321:shadowcolor=0x310f12:shadowx=5:shadowy=6:x=(w-text_w)/2:y=250`;
  if(beat.style==='norm') filter+=`,drawtext=fontfile=${font}:text='§ 113 I 4 VwGO':fontsize=105:fontcolor=white:borderw=4:bordercolor=0x076a78:shadowcolor=0x045267:shadowx=4:shadowy=5:x=(w-text_w)/2:y=110`;
  if(beat.style==='merke') filter+=`,drawtext=fontfile=${font}:text='MERKE':fontsize=91:fontcolor=white:borderw=4:bordercolor=0x057284:shadowcolor=0x064354:shadowx=3:shadowy=4:x=(w-text_w)/2:y=126,drawtext=fontfile=${fontHud}:text='ZEITPUNKT':fontsize=67:fontcolor=white:borderw=2:bordercolor=0x027181:x=(w-text_w)/2:y=300,drawtext=fontfile=${fontHud}:text='INTERESSE':fontsize=67:fontcolor=white:borderw=2:bordercolor=0x027181:x=(w-text_w)/2:y=535`;
  run('ffmpeg',['-y','-loglevel','error','-loop','1','-framerate',String(fps),'-i',input,'-vf',filter,'-frames:v',String(Math.round((beat.until-beat.at)*fps)),'-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-an',output]);
  beat.output=output;
}
let actualAt=0;
for(const beat of beats){if(fs.statSync(beat.output).size<1000)throw new Error('Segment leer: '+beat.output);beat.actualAt=actualAt;actualAt+=duration(beat.output);}
const concat=path.join(out,'concat.txt');
fs.writeFileSync(concat,beats.map(x=>`file '${x.output}'`).join('\n')+'\n');
const silent=path.join(out,'silent.mp4');
run('ffmpeg',['-y','-loglevel','error','-f','concat','-safe','0','-i',concat,'-c','copy',silent]);
if(duration(silent)<b[6]-.2)throw new Error('Video unvollständig');
async function sfx(name,prompt,seconds){
  const r=await fetch('https://api.elevenlabs.io/v1/sound-generation',{method:'POST',headers:{'xi-api-key':key,'Content-Type':'application/json'},body:JSON.stringify({text:prompt,duration_seconds:seconds,prompt_influence:.72,model_id:'eleven_text_to_sound_v2'})});
  if(!r.ok)throw new Error(`SFX ${name}: ${r.status} ${(await r.text()).slice(0,200)}`);
  const p=path.join(out,`${name}-elevenlabs.mp3`);fs.writeFileSync(p,Buffer.from(await r.arrayBuffer()));return p;
}
const shatter=await sfx('shatter','A loud sharp futuristic holographic glass SHATTER, strong bright crisp attack as a red projected prohibition sign bursts into blue shards; brief glittering digital tail, no bass thud, no music, no voices.',1.2);
const scan=await sfx('scan','A short crisp futuristic legal robot analysis scan beep, subtle bright arpeggio and tiny digital click, no voice or music.',.8);
const ms=t=>Math.max(0,Math.round(t*1000));
const hitAt=beats[2].actualAt,scanAt=beats[6].actualAt;
const filter=`[1:a]loudnorm=I=-16:TP=-1.5:LRA=11,adelay=${ms(lead)}:all=1,volume=0.7:enable='between(t,${hitAt.toFixed(3)},${(hitAt+.8).toFixed(3)})'[v];`+
  `[2:a]highpass=f=180,equalizer=f=2500:t=q:w=1.2:g=5,volume=1.55,adelay=${ms(hitAt)}:all=1[sh];`+
  `[3:a]volume=0.20,adelay=${ms(scanAt)}:all=1[sc];`+
  `[v][sh][sc]amix=inputs=3:duration=longest:normalize=0,alimiter=limit=0.87[a]`;
const destination=path.join(out,'herrjurist-2026-09-28-prueffassung.mp4');
run('ffmpeg',['-y','-loglevel','error','-i',silent,'-i',voicePath,'-i',shatter,'-i',scan,'-filter_complex',filter,'-map','0:v:0','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-t',String(b[6]),'-movflags','+faststart',destination]);
if(fs.statSync(destination).size<1000000||duration(destination)<b[6]-.2)throw new Error('MP4 unvollständig');
fs.writeFileSync(path.join(out,'timing.json'),JSON.stringify({script,spokenNumberRule:'§ 113 = Paragraf eins dreizehn; § 224 = Paragraf zwei vierundzwanzig; § 1923 = Paragraf neunzehn dreiundzwanzig',voice,model,voiceDuration,lead,boundaries:b,hitAt,scanAt,beats:beats.map(x=>({at:x.at,actualAt:x.actualAt,until:x.until,image:x.image,punch:x.punch||1,style:x.style||null}))},null,2));
console.log(`${destination}; ${duration(destination).toFixed(2)}s; hologram shatter at ${hitAt.toFixed(2)}s`);
