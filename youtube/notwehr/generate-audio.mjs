import fs from 'node:fs';
import path from 'node:path';
const key=process.env.ELEVENLABS_API_KEY;
if(!key) throw Error('ELEVENLABS_API_KEY fehlt');
const script=JSON.parse(fs.readFileSync(new URL('./script.json',import.meta.url),'utf8'));
const out=path.resolve('youtube/notwehr/audio');
fs.mkdirSync(out,{recursive:true});
const voices={
 narrator:{id:'PhufIH7nYh2Up1uej6aY',model:'eleven_multilingual_v2',voice_settings:{stability:.42,similarity_boost:.82,style:.38,use_speaker_boost:true,speed:1.08}},
 prof:{id:'dFA3XRddYScy6ylAYTIO',model:'eleven_multilingual_v2',voice_settings:{stability:.43,similarity_boost:.80,style:.40,use_speaker_boost:true,speed:1.04}},
 form7:{id:'rKiu7lQ4c5P3az3745s3',model:'eleven_multilingual_v2',voice_settings:{stability:.60,similarity_boost:.85,style:.20,use_speaker_boost:true,speed:1.02}}
};
for(const [i,seg] of script.segments.entries()){
 for(const [j,line] of seg.lines.entries()){
  const voice=voices[line.role];if(!voice) throw Error('Unknown role '+line.role);
  const name=`${String(i+1).padStart(2,'0')}-${seg.id}-${String(j+1).padStart(2,'0')}-${line.role}`;
  const r=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voice.id}/with-timestamps?output_format=mp3_44100_128`,{method:'POST',headers:{'xi-api-key':key,'Content-Type':'application/json'},body:JSON.stringify({text:line.text,model_id:voice.model,language_code:'de',voice_settings:voice.voice_settings})});
  if(!r.ok) throw Error(`${name} HTTP ${r.status} ${(await r.text()).slice(0,250)}`);
  const result=await r.json();
  fs.writeFileSync(path.join(out,name+'.mp3'),Buffer.from(result.audio_base64,'base64'));
  fs.writeFileSync(path.join(out,name+'.json'),JSON.stringify({text:line.text,role:line.role,voiceId:voice.id,model:voice.model,alignment:result.alignment||result.normalized_alignment},null,2));
  console.log(name+' complete');
 }
}
