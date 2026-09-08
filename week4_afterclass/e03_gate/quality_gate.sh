#!/bin/bash
set -euo pipefail
dir="$1"
ruff format --check "$dir"
ruff check "$dir"
(cd "$dir" && python3 -m pytest -q)
echo "ALL GREEN"
