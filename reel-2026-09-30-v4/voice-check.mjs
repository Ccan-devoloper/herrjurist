const key=process.env.ELEVENLABS_API_KEY;
if(!key)throw new Error('ELEVENLABS_API_KEY fehlt');
const r=await fetch('https://api.elevenlabs.io/v2/voices?page_size=100',
  {headers:{'xi-api-key':key}});
if(!r.ok)throw new Error(`ElevenLabs ${r.status}: ${(await r.text()).slice(0,200)}`);
const data=await r.json();
for(const v of data.voices??[]){
  const d=[v.name,v.description??'',JSON.stringify(v.labels??{})].join(' ');
  if(/deutsch|german|male|männlich|female|weiblich|young|deep|rough/i.test(d)){
    console.log(JSON.stringify({id:v.voice_id,name:v.name,description:(v.description??'').slice(0,120),labels:v.labels}));
  }
}
