#!/usr/bin/env bash
# Render tailored resume HTML to print-ready A4 PDFs using headless Chrome.
#
#   ./render-pdf.sh                        # render every version
#   ./render-pdf.sh sumup-bank-web-fullstack   # render one version
set -euo pipefail

cd "$(dirname "$0")"

CHROME="${CHROME_BIN:-$(command -v google-chrome || command -v chromium || command -v chromium-browser)}"
if [ -z "$CHROME" ]; then
  echo "No Chrome/Chromium found. Set CHROME_BIN." >&2
  exit 1
fi

# Output filename per version directory: this is what a recruiter sees, so it
# stays human-readable rather than matching the source filename.
pdf_name_for() {
  case "$1" in
    deel-backend-engineer)      echo "Yash_Prakash_Mishra_Backend_Engineer_Node.pdf" ;;
    sumup-bank-web-fullstack)   echo "Yash_Prakash_Mishra_Fullstack_Engineer_React_Node.pdf" ;;
    doctolib-dial-senior-backend) echo "Yash_Prakash_Mishra_Senior_Backend_Engineer_Node_TypeScript.pdf" ;;
    *)                          echo "Yash_Prakash_Mishra_Resume.pdf" ;;
  esac
}

render() {
  local dir="$1"
  local src="$dir/resume.html"
  local out="$dir/$(pdf_name_for "$dir")"

  [ -f "$src" ] || { echo "No $src, skipping" >&2; return 0; }

  rm -f "$out"

  # Chrome's --print-to-pdf sometimes writes the file but never exits, so run it
  # detached and wait for the output rather than waiting on the process. Those
  # lingering processes hold a profile lock, so each render needs its own.
  local profile
  profile="$(mktemp -d)"
  (timeout 90 "$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --user-data-dir="$profile" --print-to-pdf="$out" "$src" >/dev/null 2>&1 &)

  for _ in $(seq 1 60); do
    if [ -s "$out" ]; then
      sleep 1
      echo "Wrote $out"
      if command -v pdfinfo >/dev/null; then
        pdfinfo "$out" | grep -E '^Pages' | sed 's/^/  /'
      fi
      return 0
    fi
    sleep 1
  done

  echo "Failed to render $out" >&2
  return 1
}

if [ $# -gt 0 ]; then
  for dir in "$@"; do render "${dir%/}"; done
else
  for src in */resume.html; do render "$(dirname "$src")"; done
fi
