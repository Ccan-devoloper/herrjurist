import fs from 'node:fs';
import path from 'node:path';

const voiceId = 'dFA3XRddYScy6ylAYTIO';
const apiKey = process.env.ELEVENLABS_API_KEY;
const output = path.resolve('voice-output-2026-09-26-b3');
fs.mkdirSync(output, { recursive: true });

const texts = [
  'Am Abend vor der Klausur noch schnell neuen Stoff? Lass es. Das macht die Prüfungsangst oft größer. Der letzte Abend ist dafür da, den nächsten Morgen ruhig und planbar zu machen.',
  'Lege einen festen Lernstopp fest. Danach keine neue Falllösung, kein neuer Streitstand und kein hektisches Nachschlagen. Was jetzt nicht sitzt, wird in einer Nacht nicht stabil.',
  'Pack alles, was du morgen brauchst. Jede Entscheidung, die du am Morgen nicht mehr treffen musst, spart Aufmerksamkeit für die Klausur.',
  'Prüfe Anfahrt und Uhrzeit einmal, dann ist das Thema erledigt. Ein realistischer Puffer ist hilfreicher als noch zwanzig Minuten Wiederholung.',
  'Wenn du noch etwas anschauen willst, dann nur etwas Vertrautes: ein Schema, eine kurze Checkliste, ein eigener Merksatz. Ziel ist Sicherheit, nicht Stoffzuwachs.',
  'Schlaf ist keine verlorene Lernzeit. In einer langen Klausur brauchst du Konzentration, Lesegenauigkeit und Entscheidungen. Genau dafür ist Erholung Teil der Vorbereitung.',
  'Merke dir vier Punkte: Lernstopp, Sachen packen, Anreise klären, schlafen. Der letzte Abend soll dir Entscheidungen abnehmen – nicht neue Fragen aufmachen.',
];

const status = { voice_id: voiceId, model_id: 'eleven_flash_v2_5', scenes: 0, success: false };
const save = () => fs.writeFileSync(path.join(output, 'status.json'), JSON.stringify(status, null, 2));

try {
  if (!apiKey) throw new Error('ELEVENLABS_API_KEY is missing in the Examenscampus workflow');
  const headers = { 'xi-api-key': apiKey };
  const sub = await fetch('https://api.elevenlabs.io/v1/user/subscription', { headers });
  if (!sub.ok) throw new Error(`Subscription check failed: HTTP ${sub.status}`);
  const subscription = await sub.json();
  const rest = Number(subscription.character_limit || 0) - Number(subscription.character_count || 0);
  const needed = Math.ceil(texts.join('').length * .5) + 50;
  status.tier = subscription.tier;
  status.credits_before = rest;
  status.credits_reserved = needed;
  if (rest < needed) throw new Error(`Insufficient included credits: ${rest} available; at least ${needed} required`);

  const voiceRes = await fetch(`https://api.elevenlabs.io/v1/voices/${voiceId}`, { headers });
  if (voiceRes.ok) {
    const voice = await voiceRes.json();
    status.voice_name = voice.name;
    status.voice_category = voice.category;
    if (subscription.tier === 'free' && ['professional', 'shared', 'library'].includes(voice.category)) {
      throw new Error('Selected Voice Library voice is unavailable via the API on the free tier');
    }
  }
  save();

  for (const [index, text] of texts.entries()) {
    const response = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}/with-timestamps?output_format=mp3_44100_128`, {
      method: 'POST',
      headers: { ...headers, 'content-type': 'application/json' },
      body: JSON.stringify({ text, model_id: status.model_id, language_code: 'de',
        voice_settings: index === 0
          ? { stability: .34, similarity_boost: .8, style: .45, use_speaker_boost: true, speed: .97 }
          : { stability: .45, similarity_boost: .8, style: .25, use_speaker_boost: true, speed: 1.0 } }),
    });
    if (!response.ok) throw new Error(`Scene ${index + 1}: HTTP ${response.status}: ${(await response.text()).slice(0, 250)}`);
    const result = await response.json();
    if (!result.audio_base64) throw new Error(`Scene ${index + 1}: no audio returned`);
    fs.writeFileSync(path.join(output, `szene-${String(index + 1).padStart(2, '0')}.mp3`), Buffer.from(result.audio_base64, 'base64'));
    status.scenes = index + 1;
    save();
  }
  status.success = true;
  save();
} catch (error) {
  status.error = error.message;
  save();
  console.error(status.error);
  process.exitCode = 1;
}
