#!/bin/bash
# rebuild.sh — regenerate the entire site from the research layer.
# Never touches gip-tracker.xlsx. Safe to run any time.
set -e
cd "$(dirname "$0")"

echo "1/6  validating research layer"
python3 scripts/validate_research.py

echo "2/6  research index -> app-data.js, overview, tracker, scorecard, contacts, person pages"
python3 scripts/build_site.py

echo "3/6  vendor white pages"
python3 scripts/build_dashboards.py > /dev/null
python3 scripts/patch_sand.py

echo "4/6  vendor one-sheet PDFs"
python3 scripts/build_pdfs.py > /dev/null
python3 scripts/build_sand_onesheet.py > /dev/null 2>&1 || true

echo "5/6  contact white papers (PDF)"
python3 scripts/build_contact_sheets.py

echo "6/6  syncing newly researched contacts into gip-tracker.xlsx (append only)"
python3 scripts/sync_people.py

echo
echo "done. serve it with ./start-mac.command or start-windows.bat"
