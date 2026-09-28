import fs from 'node:fs';
import path from 'node:path';

const key = process.env.ELEVENLABS_API_KEY;
if (!key) throw new Error('ELEVENLABS_API_KEY fehlt.');
const script = JSON.parse(fs.readFileSync(new URL('./script.json', import.meta.url), 'utf8'));
const out = path.resolve('youtube/polizeikontrolle/audio');
fs.mkdirSync(out, {recursive: true});
const voices = {
  narrator: {id:'PhufIH7nYh2Up1uej6aY', model:'eleven_multilingual_v2', voice_settings:{stability:.42, similarity_boost:.82, style:.38, use_speaker_boost:true, speed:1.08}},
  brakk: {id:'JiW03c2Gt43XNUQAumRP', model:'eleven_v3', voice_settings:{stability:.32, similarity_boost:.78, style:.62, use_speaker_boost:true, speed:1.03}},
  zylla: {id:'xLCJR8xcZX2YjImGFyGw', model:'eleven_v3', voice_settings:{stability:.38, similarity_boost:.78, style:.58, use_speaker_boost:true, speed:1.00}}
};
for (const [index, segment] of script.segments.entries()) {
  for (const [lineIndex, line] of segment.lines.entries()) {
    const voice=voices[line.role];
    if (!voice) throw new Error(`Unknown role: ${line.role}`);
    const name=`${String(index+1).padStart(2,'0')}-${segment.id}-${String(lineIndex+1).padStart(2,'0')}-${line.role}`;
    const resp=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voice.id}/with-timestamps?output_format=mp3_44100_128`,{
      method:'POST', headers:{'xi-api-key':key,'Content-Type':'application/json'},
      body:JSON.stringify({text:line.text,model_id:voice.model,language_code:'de',voice_settings:voice.voice_settings})
    });
    if(!resp.ok) throw new Error(`${name} HTTP ${resp.status} ${(await resp.text()).slice(0,350)}`);
    const result=await resp.json();
    fs.writeFileSync(path.join(out,`${name}.mp3`),Buffer.from(result.audio_base64,'base64'));
    fs.writeFileSync(path.join(out,`${name}.json`),JSON.stringify({text:line.text,role:line.role,voiceId:voice.id,model:voice.model,alignment:result.alignment||result.normalized_alignment},null,2));
    console.log(`${name} completed`);
  }
}
