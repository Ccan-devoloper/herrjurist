import fs from 'node:fs';
import path from 'node:path';

const key=process.env.ELEVENLABS_API_KEY;
if(!key) throw new Error('ELEVENLABS_API_KEY fehlt.');
const script=JSON.parse(fs.readFileSync(new URL('./script.json',import.meta.url),'utf8'));
const out=path.resolve('youtube/angebot/audio');
fs.mkdirSync(out,{recursive:true});
const voices={
 narrator:{id:'PhufIH7nYh2Up1uej6aY',model:'eleven_multilingual_v2',voice_settings:{stability:.42,similarity_boost:.82,style:.38,use_speaker_boost:true,speed:1.08}},
 rex:{id:'TX3LPaxmHKxFdv7VOQHJ',model:'eleven_multilingual_v2',voice_settings:{stability:.39,similarity_boost:.80,style:.48,use_speaker_boost:true,speed:1.04}},
 zylla:{id:'xLCJR8xcZX2YjImGFyGw',model:'eleven_v3',voice_settings:{stability:.38,similarity_boost:.78,style:.58,use_speaker_boost:true,speed:1.00}}
};
for(const [si,seg] of script.segments.entries()){
 for(const [li,line] of seg.lines.entries()){
  const voice=voices[line.role];
  if(!voice) throw new Error(`Unbekannte Rolle: ${line.role}`);
  const name=`${String(si+1).padStart(2,'0')}-${seg.id}-${String(li+1).padStart(2,'0')}-${line.role}`;
  const resp=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voice.id}/with-timestamps?output_format=mp3_44100_128`,{
   method:'POST',headers:{'xi-api-key':key,'Content-Type':'application/json'},
   body:JSON.stringify({text:line.text,model_id:voice.model,language_code:'de',voice_settings:voice.voice_settings})
  });
  if(!resp.ok) throw new Error(`${name}: HTTP ${resp.status} ${(await resp.text()).slice(0,350)}`);
  const result=await resp.json();
  fs.writeFileSync(path.join(out,`${name}.mp3`),Buffer.from(result.audio_base64,'base64'));
  fs.writeFileSync(path.join(out,`${name}.json`),JSON.stringify({text:line.text,role:line.role,voiceId:voice.id,model:voice.model,alignment:result.alignment||result.normalized_alignment},null,2));
  console.log(`${name} fertig`);
 }
}
