import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";

import { titelZeilen, folieHtml } from "../src/vorlagen.mjs";
import { kontext } from "../src/render.mjs";
import { hookTyp } from "../src/insights.mjs";

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
  assert.match(html, /gap:5px/);
  assert.match(html, /border-radius:30px/);
});

test("Hook-Regie lässt konkrete Fragen gegen Fehler- und Nutzenhooks antreten", () => {
  const autor = fs.readFileSync(new URL("../src/autor.mjs", import.meta.url), "utf8");
  assert.match(autor, /drei alternative Titel.*konkrete juristische Frage/s);
  assert.match(autor, /echten Meta-Insights/);
  assert.match(autor, /Stoppt die Anfechtung die Vollziehung\?/);
  assert.match(autor, /HOOK_KONKRETE_FRAGE/);
  assert.match(autor, /if \(konkreteFrage\) p \+= 3/);
  assert.match(autor, /else if \(endetOffen && !hatNutzen\) p -= 4/);
  assert.match(autor, /zeilen: \{ type: "array"/);
});

test("Normfragen bleiben Fragen und werden nicht als Zahlenhook gelernt", () => {
  assert.equal(hookTyp("§ 80 Abs. 5 VwGO?"), "frage");
  assert.equal(hookTyp("Wann greift § 626 BGB?"), "frage");
  assert.equal(hookTyp("7 Themen, eine Wochenendstunde"), "zahl");
  assert.equal(hookTyp("Der Fehler bei § 122 BGB"), "fehler");
});
