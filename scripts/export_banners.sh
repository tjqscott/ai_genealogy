#!/bin/bash
set -euo pipefail

# The image-generation tool supplies a 3:1 canvas. Each new design occupies
# its central 5:1 band; this export removes only the blank delivery margins.
repo_root="$(cd "$(dirname "$0")/.." && pwd)"

for name in 01-headline 02-documents 03-newspapers 04-free-sources; do
  source_file="$repo_root/docs/artwork/$name-source.png"
  output_file="$repo_root/docs/assets/$name-5x1.png"
  source_width="$(sips --getProperty pixelWidth "$source_file" | awk '/pixelWidth:/ {print $2}')"
  source_height="$(sips --getProperty pixelHeight "$source_file" | awk '/pixelHeight:/ {print $2}')"
  export_height=$((source_width / 5))
  export_width=$((export_height * 5))
  if ((export_height <= 0 || export_height > source_height)); then
    printf 'Invalid source dimensions for %s\n' "$name" >&2
    exit 1
  fi
  sips --cropToHeightWidth "$export_height" "$export_width" "$source_file" --out "$output_file" >/dev/null
  printf '%s: %s x %s\n' "$name" "$export_width" "$export_height"
done
