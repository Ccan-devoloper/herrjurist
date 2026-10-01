#!/usr/bin/env bash
# Packt den Produktionsmaster einer Folge und lädt die Ablieferung nach Drive (rclone, Remote "lexverse").
#   bash youtube/tools/master_packen.sh FOLGENORDNER FIGURORDNER "NNN Kurztitel" NNN-Dateiname SCRATCH [THUMBORDNER] [METAORDNER]
# FOLGENORDNER: youtube/preproduction/NNN-kurzname   FIGURORDNER: youtube/preproduction/peeps/op_xx
# Erwartet in FOLGENORDNER/out: NNN-Dateiname.mp4, NNN-Dateiname-Hauptfilm.mp4, bildhalte/, Prüfbilder (*.png, render.log)
# THUMBORDNER enthält NNN.jpg und NNN_B.jpg (aus thumbnails/aus_plan.py), METAORDNER die Upload-Texte.
set -euo pipefail
F=$(cd "$1" && pwd); FIG=$(cd "$2" && pwd); ZIEL="$3"; NAME="$4"; S="$5"; T="${6:-}"; MT="${7:-}"
P=$(cd "$F/.." && pwd); R=$(cd "$P/../.." && pwd); NR=$(basename "$F" | cut -d- -f1)
M="$S/master_$NR/master_$NR"; rm -rf "$S/master_$NR"; mkdir -p "$M"/{dokumente,code/src,code/etb2,code/stimme,figuren,bildhalte,pruefung,audio,sfx,schriften,thumbnails}
for d in SZENENPLAN.md RECHTSSTAND.md ABNAHME.md CUE-TIMELINE.md bildhalt_manifest.json kapitel.json cues.json geraeusche_herkunft.json pruefbericht.json; do
  [ -f "$F/$d" ] && cp "$F/$d" "$M/dokumente/"; done
cp "$F"/src/*.py "$M/code/src/"; cp "$P"/etb2/src/*.py "$P/etb2/einrichten.sh" "$M/code/etb2/"
cp "$P"/stimme-elevenlabs/{synth_el.py,besetzung.json,README.md} "$M/code/stimme/"
cp "$FIG"/*.png "$M/figuren/"; cp "$F"/out/bildhalte/*.jpg "$M/bildhalte/"
find "$F/out" -maxdepth 1 \( -name "*.png" -o -name "*.log" -o -name "sfx_cues.json" \) -exec cp {} "$M/pruefung/" \;
cp "$F/stimme.wav" "$M/audio/"; cp -r "$F/el_cache" "$M/audio/el_cache"
if [ -f "$F/geraeusche_herkunft.json" ]; then
  python3 - "$F/geraeusche_herkunft.json" "$P/sfx3" "$M/sfx" <<'EOF'
import json, shutil, sys, os
for k in json.load(open(sys.argv[1])):
    src = os.path.join(sys.argv[2], k + ".wav")
    if os.path.exists(src): shutil.copy(src, sys.argv[3])
EOF
fi
cp "$P/humaaans/fonts/Nunito[wght].ttf" "$P/humaaans/fonts/DMSans[opsz,wght].ttf" "$R/fonts/Nunito-OFL.txt" "$M/schriften/"
[ -n "$T" ] && cp "$T"/*.png "$M/thumbnails/" 2>/dev/null || true
SHA=$(sha256sum "$F/out/$NAME.mp4" | cut -d' ' -f1)
cat > "$M/LIESMICH.txt" <<EOF
Produktionsmaster Folge $NR ($(date +%d.%m.%Y)). Neu rendern: Repository auschecken, bash youtube/preproduction/etb2/einrichten.sh,
Figuren mit code/src/figuren_*.py erzeugen, cues.json und audio/el_cache in den Folgenordner legen, im src-Ordner
python3 ../../stimme-elevenlabs/synth_el.py skript_* (nur Cache, 0 Credits), stimme_48k.wav per ffmpeg (-ac 2), sfx/*.wav nach
preproduction/sfx3/, python3 render_*.py --out ../out, dann youtube/tools/schnitt.py. MP4 SHA-256: $SHA
EOF
(cd "$S/master_$NR" && rm -f master.zip && zip -q -r master.zip "master_$NR" && unzip -tq master.zip)
U="$S/upload_$NR"; rm -rf "$U"; mkdir -p "$U"
cp "$F/out/$NAME.mp4" "$F/out/$NAME-Hauptfilm.mp4" "$S/master_$NR/master.zip" "$U/"
if [ -n "$T" ]; then cp "$T/$NR.jpg" "$U/thumb_A.jpg"; cp "$T/${NR}_B.jpg" "$U/thumb_B.jpg"; fi
if [ -n "$MT" ]; then cp "$MT"/{beschreibung.txt,kapitel.txt,untertitel.srt,metadaten.json} "$U/"; fi
D="lexverse:LexVerse Produktion/$ZIEL"
rclone copy "$U" "$D" 2>&1 | grep -v NOTICE || true
rclone check "$U" "$D" --one-way 2>&1 | grep -E "differences|matching|ERROR" || true
rclone lsl "$D" 2>&1 | grep -v NOTICE
rclone lsjson "lexverse:LexVerse Produktion" --dirs-only 2>/dev/null | python3 -c "import json,sys;[print('Ordner-ID', d['Name'], d['ID']) for d in json.load(sys.stdin) if d['Name']==sys.argv[1]]" "$ZIEL"
echo "MP4 SHA-256 $SHA"
