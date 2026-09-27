const key = process.env.ELEVENLABS_API_KEY;
if (!key) throw new Error('ELEVENLABS_API_KEY fehlt');
async function get(url) {
  const response = await fetch(url, {headers:{'xi-api-key':key}});
  if (!response.ok) throw new Error(`ElevenLabs ${response.status}: ${(await response.text()).slice(0,160)}`);
  return response.json();
}
const mine = await get('https://api.elevenlabs.io/v2/voices?page_size=100');
console.log('Verfügbare weibliche Stimmen im Konto:');
for (const voice of mine.voices ?? []) {
  const labels=voice.labels ?? {};
  if (!/female|weiblich/i.test(labels.gender??'')) continue;
  console.log(JSON.stringify({id:voice.voice_id,name:voice.name,category:voice.category,description:(voice.description??'').slice(0,160),labels}));
}
const shared = await get('https://api.elevenlabs.io/v1/shared-voices?language=de&gender=female&sort=trending&page_size=100');
console.log('Deutsche weibliche Stimmen der Voice Library (Auswahl):');
for (const voice of (shared.voices??[]).slice(0,60)) {
  console.log(JSON.stringify({id:voice.voice_id,owner:voice.public_owner_id,name:voice.name,age:voice.age,accent:voice.accent,use_case:voice.use_case,category:voice.category,description:(voice.description??'').slice(0,200)}));
}
