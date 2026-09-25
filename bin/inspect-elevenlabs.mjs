import fs from 'node:fs';
const key=process.env.ELEVENLABS_API_KEY;
if(!key) throw Error('Missing API key');
const headers={'xi-api-key':key};
const get=async path=>{
 const r=await fetch('https://api.elevenlabs.io'+path,{headers});
 if(!r.ok) throw Error(path+' HTTP '+r.status+' '+(await r.text()).slice(0,300));
 return r.json();
};
const [subscription,owned,shared]=await Promise.all([
 get('/v1/user/subscription'),get('/v1/voices'),get('/v2/voices?language=de&gender=male&page_size=50')
]);
const pick=v=>({id:v.voice_id,name:v.name,description:v.description,category:v.category,labels:v.labels,preview_url:v.preview_url});
fs.writeFileSync('voice-inspection.json',JSON.stringify({tier:subscription.tier,creditsRemaining:subscription.character_limit-subscription.character_count,owned:owned.voices.map(pick),shared:shared.voices.map(pick),hasMore:shared.has_more,nextPage:shared.next_page_token},null,2));
console.log('German male voices:',shared.voices.map(v=>v.name).join(', '));
