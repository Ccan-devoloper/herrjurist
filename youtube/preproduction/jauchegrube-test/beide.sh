set -e
cd "$(dirname "$0")/src"
for E in moritz carla; do
  cp ../cues_$E.json ../cues.json; cp ../stimme_48k_$E.wav ../stimme_48k.wav
  VIDEONAME="Jauchegrube-$E" python3 render_ja.py --out ../out 2>&1 | tail -2
done
