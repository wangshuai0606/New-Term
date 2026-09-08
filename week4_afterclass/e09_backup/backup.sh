#!/bin/bash
set -euo pipefail
src="$1"
stamp=$(date +%Y%m%d_%H%M%S)
cp "$src" "${src%.txt}_backup_${stamp}.txt"
echo "Backed up to ${src%.txt}_backup_${stamp}.txt"
