#!/bin/bash
set -euo pipefail
curl -fsS http://127.0.0.1:8000/packages.json | jq '[.[] | select(.status=="active" and .downloads>=100)] | sort_by(-.downloads, .name)' > filtered.json
{
  echo "# Active Packages Report"
  echo ""
  echo "| name | version | downloads |"
  echo "| --- | --- | --- |"
  jq -r '.[] | "| \(.name) | \(.version) | \(.downloads) |"' filtered.json
} > summary.md
echo "Generated summary.md"
