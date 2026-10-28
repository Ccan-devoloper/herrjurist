#!/bin/sh
# Lädt den Emoji-Satz "Fluent Emoji Flat" (Microsoft, MIT-Lizenz) im Iconify-Format nach assets/ (nicht im Repository).
set -e
cd "$(dirname "$0")"
mkdir -p assets && cd assets
npm pack @iconify-json/fluent-emoji-flat --silent >/dev/null
rm -rf fluent-emoji-flat && mkdir fluent-emoji-flat
tar -xzf iconify-json-fluent-emoji-flat-*.tgz -C fluent-emoji-flat --strip-components=1
rm iconify-json-fluent-emoji-flat-*.tgz
echo "Emoji-Satz: $(pwd)/fluent-emoji-flat/icons.json"
