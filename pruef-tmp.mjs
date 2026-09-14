import fs from "node:fs";
import path from "node:path";
import { beitragRendern } from "./src/render.mjs";
const SC = "/tmp/claude-0/-home-user-steuerberater/ba453c92-06f3-5de1-91a1-57a28d84ca40/scratchpad";
const b = JSON.parse(fs.readFileSync(`${SC}/b2-neu.json`, "utf8"));
const pfade = await beitragRendern({ ...b, fachLabel: "Familien- und Erbrecht" }, path.join(SC, "b2-out"), {});
console.log(pfade.map((p, i) => `${i + 1}: ${p}`).join("\n"));
