import fs from 'node:fs';
import path from 'node:path';
const key = process.env.ELEVENLABS_API_KEY;
if (!key) throw new Error('ELEVENLABS_API_KEY fehlt');
const voiceId = '2aL479c8D3QMIPExj0tw'; // Selena: deutsche, tiefere und ausdrucksstarke Frauenstimme.
const output = path.resolve('reel-test-2026-09-27/mara-voice-tests');
fs.mkdirSync(output,{recursive:true});
const takes = [
  {name:'short-ah',text:'[shouts in sudden pain] Ah!',seed:91224},
  {name:'short-au',text:'[sharp startled cry] Au!',seed:91324},
  {name:'breath-ah',text:'[gasps sharply, then cries out briefly] Ah!',seed:91424}
];
for (const take of takes) {
  const response = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}/with-timestamps?output_format=mp3_44100_128`,{
    method:'POST',headers:{'xi-api-key':key,'Content-Type':'application/json'},
    body:JSON.stringify({text:take.text,model_id:'eleven_v3',language_code:'de',seed:take.seed,
      voice_settings:{stability:0.35,similarity_boost:0.75}})
  });
  if (!response.ok) throw new Error(`${take.name}: ElevenLabs ${response.status} ${(await response.text()).slice(0,300)}`);
  const data = await response.json();
  fs.writeFileSync(path.join(output,`${take.name}.mp3`),Buffer.from(data.audio_base64,'base64'));
  fs.writeFileSync(path.join(output,`${take.name}.json`),JSON.stringify({voiceId,voiceName:'Selena',model:'eleven_v3',text:take.text,seed:take.seed,alignment:data.alignment},null,2));
  console.log(`${take.name}: ${(data.audio_base64.length*3/4/1024).toFixed(1)} KiB, Alignment ${data.alignment?.characters?.length ?? 0} Zeichen`);
}
