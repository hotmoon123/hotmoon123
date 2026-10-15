#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT/backend"
command -v python3 >/dev/null || { echo 'Install Python 3 and python3-venv first.'; exit 1; }
python3 -c 'import sys; assert sys.version_info >= (3,10), "Python 3.10+ is required"'
if [[ ! -x .venv/bin/python ]]; then python3 -m venv .venv; fi
.venv/bin/python -m pip install -r requirements.txt
printf '\nStitchLedger: http://127.0.0.1:8000\nTest data only. Stop with Ctrl+C.\n'
exec .venv/bin/uvicorn main:app --host 127.0.0.1 --port 8000
