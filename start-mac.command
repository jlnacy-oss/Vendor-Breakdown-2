#!/bin/bash
# Starts a local web server for the tracker and opens it in your browser.
# Nothing is published. The server only listens on this machine.
cd "$(dirname "$0")" || exit 1

PORT=8765
echo ""
echo "  GIP Vendor Tracker"
echo "  ------------------"
echo "  Serving this folder at http://localhost:$PORT"
echo "  Leave this window open while you use the app."
echo "  Press Ctrl+C when you're done."
echo ""

( sleep 1; open "http://localhost:$PORT/index.html" 2>/dev/null || \
  xdg-open "http://localhost:$PORT/index.html" 2>/dev/null ) &

python3 -m http.server "$PORT" --bind 127.0.0.1
