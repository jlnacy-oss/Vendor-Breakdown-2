@echo off
REM Starts a local web server for the tracker and opens it in your browser.
REM Nothing is published. The server only listens on this machine.
cd /d "%~dp0"
echo.
echo   GIP Vendor Tracker
echo   ------------------
echo   Serving this folder at http://localhost:8765
echo   Leave this window open while you use the app.
echo   Close it (or press Ctrl+C) when you're done.
echo.
start "" http://localhost:8765/index.html
python -m http.server 8765 --bind 127.0.0.1
if errorlevel 1 (
  echo.
  echo   Python was not found. Either install Python, or just open
  echo   index.html directly and use the "Load tracker" button.
  pause
)
