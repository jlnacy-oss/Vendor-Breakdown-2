@echo off
REM rebuild.bat - regenerate the entire site from the research layer.
REM Never touches gip-tracker.xlsx. Safe to run any time.
cd /d "%~dp0"
echo 1/6  validating research layer
python scripts\validate_research.py || goto :fail
echo 2/6  overview, tracker, scorecard, contacts, person pages
python scripts\build_site.py || goto :fail
echo 3/6  vendor white pages
python scripts\build_dashboards.py >nul || goto :fail
python scripts\patch_sand.py || goto :fail
echo 4/6  vendor one-sheet PDFs
python scripts\build_pdfs.py >nul || goto :fail
python scripts\build_sand_onesheet.py >nul 2>&1
echo 5/6  contact one-sheet PDFs
python scripts\build_contact_sheets.py || goto :fail
echo 6/6  syncing newly researched contacts into gip-tracker.xlsx (append only)
python scripts\sync_people.py || goto :fail
echo.
echo done. serve it with start-windows.bat
goto :eof
:fail
echo.
echo BUILD FAILED - nothing was published. See the error above.
pause
