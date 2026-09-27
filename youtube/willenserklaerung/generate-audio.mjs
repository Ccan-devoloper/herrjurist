import fs from 'node:fs';
import path from 'node:path';

const key = process.env.ELEVENLABS_API_KEY;
if (!key) throw new Error('ELEVENLABS_API_KEY fehlt; freigegebene Sprecherstimme nicht erzeugbar.');
const script = JSON.parse(fs.readFileSync(new URL('./script.json', import.meta.url), 'utf8'));
const out = path.resolve('youtube/willenserklaerung/audio');
fs.mkdirSync(out, { recursive: true });

const settings = {
  narrator: { id: 'PhufIH7nYh2Up1uej6aY', model: 'eleven_multilingual_v2', voice_settings: { stability: 0.42, similarity_boost: 0.82, style: 0.38, use_speaker_boost: true, speed: 1.08 } },
};

for (const [index, segment] of script.segments.entries()) {
  for (const [lineIndex, line] of segment.lines.entries()) {
    if (line.role !== 'narrator') continue;
    const voice = settings[line.role];
    const basename = `${String(index + 1).padStart(2, '0')}-${segment.id}-${String(lineIndex + 1).padStart(2, '0')}`;
    if (process.env.HERR_JURIST_AUDIO_ONLY && basename !== process.env.HERR_JURIST_AUDIO_ONLY) continue;
    const response = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voice.id}/with-timestamps?output_format=mp3_44100_128`, {
      method: 'POST',
      headers: { 'xi-api-key': key, 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: line.text, model_id: voice.model, language_code: 'de', voice_settings: voice.voice_settings }),
    });
    if (!response.ok) throw new Error(`Sprachgenerierung ${basename}: HTTP ${response.status} ${(await response.text()).slice(0, 300)}`);
    const result = await response.json();
    fs.writeFileSync(path.join(out, `${basename}.mp3`), Buffer.from(result.audio_base64, 'base64'));
    fs.writeFileSync(path.join(out, `${basename}.json`), JSON.stringify({ text: line.text, voice: line.role, voiceId: voice.id, model: voice.model, alignment: result.alignment || result.normalized_alignment }, null, 2));
    console.log(`${basename}: Sprachdatei und Zeichenzeiten erstellt`);
  }
}
