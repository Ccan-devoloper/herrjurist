#!/usr/bin/env bash
# Baut die lokale Render-Umgebung der Open-Peeps-Videos (Serienstandard Katzenkönig) unter youtube/preproduction/ auf.
# Alles hier ist aus freien Quellen reproduzierbar und per .gitignore aus dem Repository ausgeschlossen.
#   bash youtube/preproduction/etb2/einrichten.sh
set -euo pipefail
P="$(cd "$(dirname "$0")/.." && pwd)"          # youtube/preproduction
R="$(cd "$P/../.." && pwd)"                     # Repository
cd "$P"

pip install -q pillow numpy scipy cairosvg svgpathtools imageio-ffmpeg lxml fonttools 2>&1 | grep -v WARNING || true

# Schriften: Nunito (Repo, SIL OFL) und DM Sans als Ersatz (google/fonts, SIL OFL)
mkdir -p humaaans/fonts
cp "$R/fonts/Nunito.ttf" "humaaans/fonts/Nunito[wght].ttf"
[ -s "humaaans/fonts/DMSans[opsz,wght].ttf" ] || curl -sSfL -o "humaaans/fonts/DMSans[opsz,wght].ttf" \
  "https://raw.githubusercontent.com/google/fonts/main/ofl/dmsans/DMSans%5Bopsz%2Cwght%5D.ttf"

# Icon-Bibliotheken (Iconify-JSON): Tabler, Phosphor, Fluent Emoji (MIT), Pepicons (CC BY 4.0), MingCute (Apache 2.0), Streamline Freehand (CC BY 4.0)
mkdir -p blasen
for s in tabler ph fluent-emoji-flat fluent-emoji-high-contrast pepicons-pop pepicons-pencil mingcute streamline-freehand; do
  [ -f "blasen/$s/package/icons.json" ] && continue
  (cd blasen && npm pack -s "@iconify-json/$s" >/dev/null && mkdir -p "$s" && tar xzf iconify-json-$s-*.tgz -C "$s" && rm iconify-json-$s-*.tgz)
done

# Pinselblasen (Comical.js + perfect-freehand), Quelle: hypothek-zweiterwerb-test/blasen
mkdir -p bl2
cp hypothek-zweiterwerb-test/blasen/{blase_e.js,blase_c.js,leer.html,package.json} bl2/   # blase_c.js = Sprechblasen Stil C (eine Kontur, Keil-Schwanz)
(cd bl2 && npm i -s --no-audit --no-fund >/dev/null \
  && sed 's/const tailWidth = 18;/const tailWidth = window.TAILW || 18;/' node_modules/comicaljs/dist/index.js > comical_p.js \
  && { printf 'var PF={};(function(exports){'; cat node_modules/perfect-freehand/dist/cjs/index.js; printf '\n})(PF);\n'; } > pf.js)
CHROME=$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome 2>/dev/null | head -1)
[ -n "$CHROME" ] && sed -i "s#executablePath: '[^']*'#executablePath: '$CHROME'#" bl2/blase_e.js bl2/blase_c.js

mkdir -p peeps sfx3
echo "Render-Umgebung bereit: $P (etb2/src, humaaans/fonts, blasen, bl2, peeps, sfx3)"
