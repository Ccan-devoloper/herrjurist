const key=process.env.ELEVENLABS_API_KEY;
if(!key) throw Error('Missing ElevenLabs secret');
const r=await fetch('https://api.elevenlabs.io/v1/voices',{headers:{'xi-api-key':key}});
if(!r.ok) throw Error('ElevenLabs voices '+r.status);
const j=await r.json();
const list=j.voices.map(v=>({id:v.voice_id,name:v.name,description:v.description,labels:v.labels,category:v.category,verified_languages:v.verified_languages}));
console.log(JSON.stringify(list,null,2));
