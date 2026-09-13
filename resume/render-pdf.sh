#!/usr/bin/env bash
# Render the HTML resume to a print-ready A4 PDF using headless Chrome.
set -euo pipefail

cd "$(dirname "$0")"
SRC="yash-mishra-deel-backend-engineer.html"
OUT="yash-mishra-deel-backend-engineer.pdf"

CHROME="${CHROME_BIN:-$(command -v google-chrome || command -v chromium || command -v chromium-browser)}"

rm -f "$OUT"

# Chrome's --print-to-pdf sometimes writes the file but never exits, so run it
# detached and wait for the output instead of waiting on the process.
(timeout 90 "$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf="$OUT" "$SRC" >/dev/null 2>&1 &)

for _ in $(seq 1 60); do
  if [ -s "$OUT" ]; then
    sleep 1
    echo "Wrote $OUT"
    command -v pdfinfo >/dev/null && pdfinfo "$OUT" | grep -E '^(Pages|Page size)'
    exit 0
  fi
  sleep 1
done

echo "Failed to render $OUT" >&2
exit 1
