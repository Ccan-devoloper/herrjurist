#!/usr/bin/env bash
# Richtet die Render-Umgebung der Open-Peeps-Vorproduktion ein (Ressourcenordner $OP_RES, Standard op/.res).
# Alles stammt aus freien Quellen: Nunito, DM Sans, Liberation (SIL OFL), Open Peeps (CC0), Iconify-Sets
# Tabler, Phosphor, Fluent Emoji (MIT), MingCute (Apache 2.0), Pepicons, Streamline Freehand (CC BY 4.0),
# Comical.js und perfect-freehand (MIT). Der Ressourcenordner ist per .gitignore ausgeschlossen.
#   bash op/einrichten.sh
set -euo pipefail
HIER="$(cd "$(dirname "$0")" && pwd)"
RES="${OP_RES:-$HIER/.res}"
mkdir -p "$RES/fonts" "$RES/blasen" "$RES/bl2" "$RES/peeps/op_ec" "$RES/cache"

python3 -m pip install -q -r "$HIER/requirements.txt" 2>&1 | grep -v -i "warning\|notice" || true

cp "$HIER"/ressourcen/fonts/*.ttf "$RES/fonts/"
[ -f "$RES/fonts/Caveat.ttf" ] || cp "$HIER/../fonts/Caveat.ttf" "$RES/fonts/Caveat.ttf"

for s in tabler ph fluent-emoji-flat fluent-emoji-high-contrast pepicons-pop pepicons-pencil mingcute streamline-freehand; do
  [ -f "$RES/blasen/$s/package/icons.json" ] && continue
  (cd "$RES/blasen" && npm pack -s "@iconify-json/$s" >/dev/null && mkdir -p "$s" && tar xzf iconify-json-$s-*.tgz -C "$s" && rm iconify-json-$s-*.tgz)
done

cp "$HIER"/ressourcen/blasen-js/{blase_e.js,leer.html,package.json} "$RES/bl2/"
if [ ! -f "$RES/bl2/comical_p.js" ]; then
  (cd "$RES/bl2" && npm i -s --no-audit --no-fund >/dev/null \
    && sed 's/const tailWidth = 18;/const tailWidth = window.TAILW || 18;/' node_modules/comicaljs/dist/index.js > comical_p.js \
    && { printf 'var PF={};(function(exports){'; cat node_modules/perfect-freehand/dist/cjs/index.js; printf '\n})(PF);\n'; } > pf.js)
fi
echo "Render-Umgebung bereit: $RES"
