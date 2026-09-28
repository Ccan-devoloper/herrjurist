#!/usr/bin/env node
import fs from "node:fs";
import { spawnSync } from "node:child_process";

const text = "Der Katzenkönig-Fall ist ein Klassiker zur Abgrenzung von Anstiftung und mittelbarer Täterschaft. H. und P. brachten den leicht beeinflussbaren R. durch Tricks und mystische Inszenierungen dazu, an den Katzenkönig zu glauben. Später täuschten sie ihm vor, der Katzenkönig verlange ein Menschenopfer, sonst würden Millionen sterben. R. wusste zwar, dass Töten verboten ist, glaubte aber, wegen der angeblichen Rettung der Menschheit handeln zu dürfen. Der BGH sah darin einen vermeidbaren Verbotsirrtum. Trotzdem konnten H. und P. mittelbare Täter sein, weil sie den Irrtum hervorgerufen, gezielt ausgenutzt und die Tat gesteuert hatten. Merksatz: Beim vermeidbaren Verbotsirrtum des Vordermanns mittelbare Täterschaft nicht vorschnell ablehnen. Entscheidend sind Art und Tragweite des Irrtums, Intensität der Einwirkung und objektive Tatherrschaft.";
fs.mkdirSync("out/katzenkoenig-audio", { recursive: true });

async function elf() {
  const key = process.env.ELEVENLABS_API_KEY;
  const id = process.env.ELEVENLABS_VOICE_ID;
  if (!key || !id) return false;
  const model = process.env.ELEVENLABS_MODEL || "eleven_flash_v2_5";
  const res = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${encodeURIComponent(id)}?output_format=mp3_44100_128`, {
    method: "POST",
    headers: { "xi-api-key": key, "Content-Type": "application/json" },
    body: JSON.stringify({
      text,
      model_id: model,
      language_code: "de",
      voice_settings: { stability: 0.42, similarity_boost: 0.82, style: 0.38, use_speaker_boost: true, speed: 1.02 }
    })
  });
  if (!res.ok) {
    console.warn("ElevenLabs fehlgeschlagen:", res.status, (await res.text()).slice(0,300));
    return false;
  }
  fs.writeFileSync("out/katzenkoenig-audio/narration.mp3", Buffer.from(await res.arrayBuffer()));
  console.log("ElevenLabs-Audio erzeugt.");
  return true;
}

function piper() {
  const model = process.env.PIPER_MODEL;
  if (!model || !fs.existsSync(model)) throw new Error("Kein ElevenLabs-Voice und kein Piper-Modell.");
  const wav = "out/katzenkoenig-audio/narration.wav";
  const r = spawnSync("piper", ["-m", model, "-f", wav, "--length-scale", "1.03", "--sentence-silence", "0.12"], { input: text, encoding: "utf8" });
  if (r.status !== 0) throw new Error(r.stderr || "Piper fehlgeschlagen");
  const f = spawnSync("ffmpeg", ["-y","-loglevel","error","-i",wav,"-af","aresample=44100,loudnorm=I=-16:TP=-1.5:LRA=9","-c:a","libmp3lame","-q:a","2","out/katzenkoenig-audio/narration.mp3"], { encoding:"utf8" });
  if (f.status !== 0) throw new Error(f.stderr || "ffmpeg fehlgeschlagen");
  console.log("Piper-Fallback-Audio erzeugt.");
}

if (!(await elf())) piper();
fs.writeFileSync("out/katzenkoenig-audio/script.txt", text + "\n");
