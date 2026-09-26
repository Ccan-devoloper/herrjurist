import fs from 'node:fs';
const key=process.env.ELEVENLABS_API_KEY;
if(!key)throw Error('Missing API key');
const candidates=[
 ['Moritz','PhufIH7nYh2Up1uej6aY'],
 ['Johannes','r8MyP4qUsq5WFFSkPdfV'],
 ['Helmut','dFA3XRddYScy6ylAYTIO']
];
const text='Paragraf einhundertdreizehn Absatz eins Satz vier der Verwaltungsgerichtsordnung. Bei der Fortsetzungsfeststellungsklage musst du das Fortsetzungs-Feststellungs-Interesse prüfen. Und Paragraf einhundertsechsunddreißig a der Strafprozessordnung verbietet die Verwertung selbst bei Zustimmung.';
fs.mkdirSync('voice-test-de',{recursive:true});
for(const [name,id] of candidates){
 const res=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${id}?output_format=mp3_44100_128`,{
  method:'POST',headers:{'xi-api-key':key,'content-type':'application/json'},
  body:JSON.stringify({text,model_id:'eleven_multilingual_v2',language_code:'de',voice_settings:{stability:.43,similarity_boost:.82,style:.4,use_speaker_boost:true,speed:1.06}})
 });
 if(!res.ok)throw Error(name+' HTTP '+res.status+' '+(await res.text()).slice(0,300));
 fs.writeFileSync(`voice-test-de/${name}.mp3`,Buffer.from(await res.arrayBuffer()));
 console.log(name,'generated');
}
const transcripts={};
for(const [name] of candidates){
 const data=new globalThis.FormData();
 data.append('model_id','scribe_v2');
 data.append('file',new globalThis.Blob([fs.readFileSync(`voice-test-de/${name}.mp3`)],{type:'audio/mpeg'}),`${name}.mp3`);
 const res=await fetch('https://api.elevenlabs.io/v1/speech-to-text',{method:'POST',headers:{'xi-api-key':key},body:data});
 if(!res.ok)throw Error(name+' transcription HTTP '+res.status+' '+(await res.text()).slice(0,300));
 transcripts[name]=(await res.json()).text;
 console.log(name,'transcribed');
}
fs.writeFileSync('voice-test-de/transcripts.json',JSON.stringify({expected:text,transcripts},null,2));
