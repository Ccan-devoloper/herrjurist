import fs from 'node:fs';
import path from 'node:path';

const voiceId = 'dFA3XRddYScy6ylAYTIO';
const batch = Number(process.env.REEL_VOICE_BATCH || 0);
const dates = Array.from({length: 14}, (_,i) => new Date(Date.UTC(2026,8,27+i)).toISOString().slice(0,10));
const selected = dates.slice(batch*7,batch*7+7);
const key = process.env.ELEVENLABS_API_KEY;
if (!key) throw new Error('ELEVENLABS_API_KEY missing');
const dir = path.resolve('voice-output-27-onward', 'batch-'+batch);
fs.mkdirSync(dir,{recursive:true});
const status = {batch,dates:selected,voiceId,completed:[],success:false};
const save=()=>fs.writeFileSync(path.join(dir,'status.json'),JSON.stringify(status,null,2));
const pause=(ms)=>new Promise(resolve=>setTimeout(resolve,ms));
const headers={'xi-api-key':key};
const sceneSettings=(text,i,count)=>{
  if(i===0) return {stability:.34,similarity_boost:.82,style:.56,use_speaker_boost:true,speed:1.07};
  if(i===count-1) return {stability:.43,similarity_boost:.82,style:.42,use_speaker_boost:true,speed:1.07};
  if(/Gefahr|verbot|droh|falsch|Angriff|Schaden|ausnutz|verweigert|nicht/.test(text))
    return {stability:.39,similarity_boost:.82,style:.51,use_speaker_boost:true,speed:1.09};
  return {stability:.48,similarity_boost:.82,style:.3,use_speaker_boost:true,speed:1.11};
};
try{
  const scripts=[];
  for(const date of selected){
    const url='https://raw.githubusercontent.com/Ccan-devoloper/herrjurist/instagram-assets/vorproduktion/'+date+'.json';
    const response=await fetch(url);
    if(!response.ok)throw new Error(date+' source HTTP '+response.status);
    const tag=await response.json();
    const scenes=tag.inhalte?.b3?.szenen;
    if(!Array.isArray(scenes)||scenes.length<5)throw new Error(date+' has no valid b3 scenes');
    scripts.push({date,scenes});
  }
  const subscription=await fetch('https://api.elevenlabs.io/v1/user/subscription',{headers});
  if(!subscription.ok)throw new Error('Subscription HTTP '+subscription.status);
  const sub=await subscription.json();
  const needed=Math.ceil(scripts.flatMap(x=>x.scenes).map(s=>s.sprecher||'').join('').length*.5)+1000;
  const remaining=Number(sub.character_limit||0)-Number(sub.character_count||0);
  status.tier=sub.tier;status.includedCreditsBefore=remaining;status.reserveForBatch=needed;
  if(remaining<needed)throw new Error('Not enough included Creator credits; need '+needed+', have '+remaining);
  save();
  for(const {date,scenes} of scripts){
    const target=path.join(dir,date);
    fs.mkdirSync(target,{recursive:true});
    for(let i=0;i<scenes.length;i++){
      const text=String(scenes[i].sprecher||'').trim();
      if(!text)throw new Error(date+' scene '+(i+1)+' without voice script');
      const settings=sceneSettings(text,i,scenes.length);
      let data;
      for(let attempt=0;attempt<5;attempt++){
        const res=await fetch('https://api.elevenlabs.io/v1/text-to-speech/'+voiceId+'?output_format=mp3_44100_128',{
          method:'POST',headers:{...headers,'content-type':'application/json'},
          body:JSON.stringify({text,model_id:'eleven_flash_v2_5',language_code:'de',voice_settings:settings}),
        });
        if(res.ok){data=Buffer.from(await res.arrayBuffer());break}
        const body=(await res.text()).slice(0,250);
        if(attempt===4||![429,500,502,503,504].includes(res.status))
          throw new Error(date+' scene '+(i+1)+' TTS HTTP '+res.status+': '+body);
        await pause(3000*2**attempt);
      }
      fs.writeFileSync(path.join(target,'szene-'+String(i+1).padStart(2,'0')+'.mp3'),data);
      status.completed.push({date,scene:i+1,bytes:data.length,settings});
      save();
      console.log(date+' scene '+(i+1)+'/'+scenes.length+': '+data.length+' bytes');
    }
  }
  status.success=true;save();
}catch(error){
  status.error=error.message;save();console.error(error);process.exitCode=1;
}
