import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";

import { titelZeilen, folieHtml } from "../src/vorlagen.mjs";
import { kontext } from "../src/render.mjs";

test("Cover-Titel werden in semantische, kurze Zeilen zerlegt", () => {
  assert.deepEqual(
    titelZeilen("§ 80 Abs. 5 VwGO? Erst Vollziehung prüfen"),
    ["§ 80 Abs. 5 VwGO?", "Erst Vollziehung", "prüfen"],
  );
  assert.deepEqual(
    titelZeilen("Zulässigkeit kommt vor Begründetheit"),
    ["Zulässigkeit", "kommt vor", "Begründetheit"],
  );
  assert.deepEqual(
    titelZeilen("Besitz ist nicht automatisch Eigentum"),
    ["Besitz", "ist nicht automatisch", "Eigentum"],
  );
});

test("Autoren-Zeilen werden als getrennte kompakte Titelpillen gerendert", () => {
  const html = folieHtml({
    art: "titel",
    titel: "§ 80 Abs. 5 VwGO? Erst Vollziehung prüfen",
    titelZeilen: ["§ 80 Abs. 5 VwGO?", "Erst Vollziehung", "prüfen"],
    icon: "dokument",
  }, kontext({ fach: "oeffentlich", klausur: 3 }), 1, 6);

  assert.match(html, /titel-stack/);
  assert.equal((html.match(/class="titel-zeile"/g) || []).length, 3);
  assert.match(html, /gap:8px/);
  assert.match(html, /border-radius:28px/);
});

test("Hook-Regie belohnt Sofortnutzen statt nackter offener Frage", () => {
  const autor = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  assert.match(autor, /Slide 1 ist der Scroll-Stopper/);
  assert.match(autor, /§ 80 Abs\. 5 VwGO\? Erst Vollziehung prüfen/);
  assert.match(autor, /HOOK_NUTZEN/);
  assert.match(autor, /endetOffen && !hatNutzen/);
  assert.match(autor, /zeilen: \{ type: "array"/);
});
