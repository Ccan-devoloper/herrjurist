import fs from 'node:fs';
import path from 'node:path';
import {normGesprochen} from '../src/normen.mjs';

const batch=Number(process.env.REEL_VOICE_BATCH||0);
const voiceId=process.env.REEL_VOICE_ID||'PhufIH7nYh2Up1uej6aY';
const key=process.env.ELEVENLABS_API_KEY;
if(!key)throw Error('ELEVENLABS_API_KEY missing');
const dates=Array.from({length:14},(_,i)=>new Date(Date.UTC(2026,8,27+i)).toISOString().slice(0,10));
const selected=dates.slice(batch*7,batch*7+7);
const root=path.resolve('voice-output-corrected',`batch-${batch}`);
fs.mkdirSync(root,{recursive:true});
const status={batch,dates:selected,voiceId,model:'eleven_multilingual_v2',completed:[],success:false};
const save=()=>fs.writeFileSync(path.join(root,'status.json'),JSON.stringify(status,null,2));
const one=['null','eins','zwei','drei','vier','fünf','sechs','sieben','acht','neun','zehn','elf','zwölf','dreizehn','vierzehn','fünfzehn','sechzehn','siebzehn','achtzehn','neunzehn'];
const tens=['','','zwanzig','dreißig','vierzig','fünfzig','sechzig','siebzig','achtzig','neunzig'];
function germanNumber(n){
 if(n<20)return one[n];
 if(n<100)return n%10?((n%10===1?'ein':one[n%10])+'und'+tens[Math.floor(n/10)]):tens[n/10];
 if(n<1000)return (n<200?'ein':one[Math.floor(n/100)])+'hundert'+(n%100?germanNumber(n%100):'');
 return (n<2000?'ein':one[Math.floor(n/1000)])+'tausend'+(n%1000?germanNumber(n%1000):'');
}
function spoken(raw){
 let out=normGesprochen(raw);
 out=out.replace(/\b(Paragraf(?:en)?|Artikel|Absatz|Satz|Nummer|Halbsatz)\s+(\d{1,4})([a-z])?\b/gi,(_,label,digit,letter)=>`${label} ${germanNumber(Number(digit))}${letter?' '+letter:''}`);
 out=out.replace(/\bFortsetzungsfeststellungsinteresse\b/gi,'Fortsetzungs-Feststellungs-Interesse');
 out=out.replace(/\bVA\b/g,'Verwaltungsakt');
 out=out.replace(/\bGbR\b/g,'Gesellschaft bürgerlichen Rechts');
 if(/[§\d](?=\s*(?:StGB|BGB|StPO))/.test(out))throw Error('Unnormalized norm: '+out);
 return out;
}
const headers={'xi-api-key':key};
const pause=(ms)=>new Promise(resolve=>setTimeout(resolve,ms));
async function getJSON(url){const r=await fetch(url,{headers});if(!r.ok)throw Error('GET '+url+' HTTP '+r.status);return r.json()}
async function tts(text,settings){
 for(let attempt=0;attempt<5;attempt++){
  const r=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}?output_format=mp3_44100_128`,{
   method:'POST',headers:{...headers,'content-type':'application/json'},
   body:JSON.stringify({text,model_id:'eleven_multilingual_v2',language_code:'de',voice_settings:settings})});
  if(r.ok)return Buffer.from(await r.arrayBuffer());
  const body=(await r.text()).slice(0,250);
  if(attempt===4||![429,500,502,503,504].includes(r.status))throw Error('TTS HTTP '+r.status+' '+body);
  await pause(2500*2**attempt);
 }
}
async function transcribe(bytes){
 const body=new globalThis.FormData();body.append('model_id','scribe_v2');body.append('file',new globalThis.Blob([bytes],{type:'audio/mpeg'}),'scene.mp3');
 const r=await fetch('https://api.elevenlabs.io/v1/speech-to-text',{method:'POST',headers,body});
 if(!r.ok)throw Error('Transcription HTTP '+r.status+' '+(await r.text()).slice(0,250));
 return (await r.json()).text;
}
const sceneSettings=(text,i,count)=>({
 stability:i===0?.36:i===count-1?.48:/Gefahr|verbot|droh|falsch|Angriff|Schaden|nicht/.test(text)?.42:.49,
 similarity_boost:.82,style:i===0?.50:i===count-1?.35:/Gefahr|verbot|droh|falsch|Angriff|Schaden|nicht/.test(text)?.45:.28,
 use_speaker_boost:true,speed:i===0?1.06:1.08
});
try{
 const scripts=[];
 for(const date of selected){
  const response=await fetch(`https://raw.githubusercontent.com/Ccan-devoloper/herrjurist/instagram-assets/vorproduktion/${date}.json`);
  if(!response.ok)throw Error(date+' source HTTP '+response.status);
  const tag=await response.json();const scenes=tag.inhalte?.b3?.szenen;
  if(!Array.isArray(scenes)||scenes.length<5)throw Error(date+' missing scenes');
  scripts.push({date,scenes});
 }
 const texts=scripts.flatMap(x=>x.scenes.map(s=>spoken(String(s.sprecher||'').trim())));
 const sub=await getJSON('https://api.elevenlabs.io/v1/user/subscription');
 const remaining=Number(sub.character_limit||0)-Number(sub.character_count||0);
 const needed=texts.join('').length+5000;
 status.tier=sub.tier;status.includedCreditsBefore=remaining;status.reserveForBatch=needed;
 if(remaining<needed)throw Error(`Not enough included credits for batch ${batch}; need ${needed}, have ${remaining}`);
 save();
 for(const {date,scenes} of scripts){
  const dir=path.join(root,date);fs.mkdirSync(dir,{recursive:true});
  for(let i=0;i<scenes.length;i++){
   const text=spoken(String(scenes[i].sprecher||'').trim());
   if(!text)throw Error(date+' empty scene '+(i+1));
   const settings=sceneSettings(text,i,scenes.length);
   const bytes=await tts(text,settings);
   fs.writeFileSync(path.join(dir,`szene-${String(i+1).padStart(2,'0')}.mp3`),bytes);
   let transcript=null;
   if(i===0||/Paragraf|Fortsetzungs-|Rechtswegerschöpfung|Subsidiarität|Gesellschaft bürgerlichen Rechts/i.test(text))transcript=await transcribe(bytes);
   status.completed.push({date,scene:i+1,spokenText:text,transcript,bytes:bytes.length,settings});save();
   console.log(date+' scene '+(i+1)+'/'+scenes.length+' generated');
  }
 }
 status.success=true;save();
}catch(error){status.error=error.message;save();console.error(error);process.exitCode=1}
