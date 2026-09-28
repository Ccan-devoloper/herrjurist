import fs from 'node:fs';
import path from 'node:path';

const episode = process.argv[2];
if (!/^\d\d$/.test(episode)) throw new Error('Episode number required');
const key = process.env.ELEVENLABS_API_KEY;
if (!key) throw new Error('ELEVENLABS_API_KEY fehlt');
const root = path.resolve(`youtube/episodes/${episode}`);
const script = JSON.parse(fs.readFileSync(path.join(root, 'script.json'), 'utf8'));
const out = path.join(root, 'audio');
fs.mkdirSync(out, {recursive: true});

const voices = {
  narrator: ['PhufIH7nYh2Up1uej6aY', 'eleven_multilingual_v2', .42, .82, .38, 1.08],
  rex: ['TX3LPaxmHKxFdv7VOQHJ', 'eleven_multilingual_v2', .39, .80, .48, 1.04],
  zylla: ['xLCJR8xcZX2YjImGFyGw', 'eleven_v3', .38, .78, .58, 1.00],
  brakk: ['JiW03c2Gt43XNUQAumRP', 'eleven_v3', .32, .78, .62, 1.03],
  mara: ['VU8IqX1jR115XHqBQttd', 'eleven_multilingual_v2', .43, .79, .48, 1.03],
  prof: ['dFA3XRddYScy6ylAYTIO', 'eleven_multilingual_v2', .48, .80, .38, 1.00],
  form7: ['rKiu7lQ4c5P3az3745s3', 'eleven_multilingual_v2', .55, .80, .28, 1.00]
};
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
for (const [si, segment] of script.segments.entries()) {
  for (const [li, line] of segment.lines.entries()) {
    const v = voices[line.role];
    if (!v) throw new Error('Unknown role ' + line.role);
    const name = `${String(si + 1).padStart(2, '0')}-${segment.id}-${String(li + 1).padStart(2, '0')}-${line.role}`;
    const payload = {
      text: line.text, model_id: v[1], language_code: 'de',
      voice_settings: {stability: v[2], similarity_boost: v[3], style: v[4], use_speaker_boost: true, speed: v[5]}
    };
    let result;
    for (let attempt = 0; attempt < 6; attempt++) {
      const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${v[0]}/with-timestamps?output_format=mp3_44100_128`, {
        method: 'POST', headers: {'xi-api-key': key, 'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
      });
      if (resp.ok) { result = await resp.json(); break; }
      const detail = (await resp.text()).slice(0, 400);
      if (attempt === 5 || ![429, 500, 502, 503, 504].includes(resp.status))
        throw new Error(`${name}: HTTP ${resp.status} ${detail}`);
      await sleep((attempt + 1) * 5000);
    }
    const alignment = result.alignment || result.normalized_alignment;
    if (!result.audio_base64 || !alignment?.characters?.length) throw new Error(name + ': missing audio or alignment');
    fs.writeFileSync(path.join(out, name + '.mp3'), Buffer.from(result.audio_base64, 'base64'));
    fs.writeFileSync(path.join(out, name + '.json'), JSON.stringify({text: line.text, role: line.role, voiceId: v[0], model: v[1], alignment}, null, 2));
    console.log(name + ' fertig');
  }
}
