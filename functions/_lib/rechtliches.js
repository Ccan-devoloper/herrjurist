// Impressum und Datenschutz für die Wochenbrief-Landingpage. Die Pflichtangaben (§ 5 DDG, Art. 13 DSGVO)
// kommen aus den Pages-Variablen, NICHT aus dem Repository: eine Anschrift gehört nicht in ein öffentliches Repo.
//   ANBIETER  = "Vorname Nachname"   ANSCHRIFT = "Straße 1, 12345 Ort"   KONTAKT = "kontakt@…"
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);

export function angaben(env) {
  const fehlt = !env.ANBIETER || !env.ANSCHRIFT || !env.KONTAKT;
  return {
    fehlt,
    block: fehlt
      ? `<p class="hinweis">Angaben werden gerade ergänzt.</p>`
      : `<p>${esc(env.ANBIETER)}<br>${esc(env.ANSCHRIFT).replace(/,\s*/g, "<br>")}<br>E-Mail: <a href="mailto:${esc(env.KONTAKT)}">${esc(env.KONTAKT)}</a></p>`,
  };
}

export function seite(titel, inhalt) {
  return new Response(`<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>${titel} · LexVerse by herrjurist</title>
<style>
  @font-face{font-family:Nunito;font-weight:400 799;src:url(/fonts/nunito-700.woff2) format("woff2")}
  @font-face{font-family:Nunito;font-weight:800 1000;src:url(/fonts/nunito-900.woff2) format("woff2")}
  body{max-width:46rem;margin:0 auto;padding:1.5rem 1.25rem 3rem;background:#fffbe6;color:#16161d;font:600 16px/1.6 Nunito,system-ui,sans-serif}
  header{font-weight:900;margin-bottom:2rem}header a{color:inherit;text-decoration:none}header span{color:#7c5cff}
  h1{font-size:1.8rem;line-height:1.2;font-weight:900}h2{font-size:1.15rem;margin-top:2rem;font-weight:900}
  p,li{margin:.5rem 0}a{color:#7c5cff}
  .hinweis{border-left:3px solid #ff7a45;padding-left:1rem;color:#5c5c68}
  footer{margin-top:3rem;color:#5c5c68;font-size:.9rem}footer a{color:inherit;margin-right:1rem}
</style>
</head>
<body>
<header><a href="/">Lex<span>Verse</span> · by herrjurist</a></header>
${inhalt}
<footer><a href="/">Zur Startseite</a><a href="/impressum">Impressum</a><a href="/datenschutz">Datenschutz</a></footer>
</body>
</html>`, { headers: { "content-type": "text/html; charset=utf-8", "cache-control": "public, max-age=3600" } });
}
