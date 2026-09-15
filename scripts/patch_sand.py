# -*- coding: utf-8 -*-
"""
patch_sand.py — Sand Technologies' dashboard was hand-built before the
data-driven pipeline existed, so it isn't regenerated from vendor_data.py.
This splices the app's nav, CSS and GIP engagement blocks into it without
touching its deeper research content. Idempotent: re-running does nothing.
"""
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
PAGE = os.path.join(ROOT, "sand-technologies-dashboard.html")
MARK = "<!-- gip-app-patched -->"

APP_CSS = open(os.path.join(SCRIPT_DIR, "app.css")).read()

SECTIONS = """
  <section>
    <div class="sec-head"><span class="sec-num">06</span><h2>GIP engagement</h2></div>
    <div class="sec-note">Live from your tracker workbook. Nothing here is published or uploaded.</div>
    <div id="gip-loadbar" class="loadbar">Reading gip-tracker.xlsx&hellip;</div>
    <div class="gip-panel" id="gip-panel" data-vendor="Sand Technologies"></div>
  </section>

  <section>
    <div class="sec-head"><span class="sec-num">07</span><h2>Contacts</h2></div>
    <div class="sec-note">Each card opens that person's dashboard, which links to their downloadable
    white paper. <a href="people.html?vendor=sand-technologies" style="color:var(--steel);">All Sand Technologies contacts &rarr;</a></div>
    <div class="card-grid" id="gip-people"></div>
    <div id="nopeople" class="empty" style="display:none;"><b>No contacts on file</b>Add rows for Sand Technologies on the People sheet.</div>
  </section>

"""

SCRIPTS = """<script src="xlsx.full.min.js"></script>
<script src="gip-loader.js"></script>
<script src="app-data.js"></script>
<script src="gip-panel.js"></script>
</body>"""

NAV = ('<a class="back-link" href="index.html">&larr; All vendors</a>'
       '&nbsp;&nbsp;<a class="back-link" href="tracker.html">Engagement tracker</a>'
       '&nbsp;&nbsp;<a class="back-link" href="scorecard.html">Scorecard</a>'
       '&nbsp;&nbsp;<a class="back-link" href="people.html">All contacts</a>')


def main():
    if not os.path.exists(PAGE):
        print("sand dashboard not found — skipping")
        return
    html = open(PAGE).read()
    if MARK in html:
        print("sand dashboard already patched")
        return

    html = html.replace("</style>", APP_CSS + "\n</style>", 1)

    # keep the site fully offline: use the vendored Chart.js build
    html = html.replace(
        "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js",
        "chart.umd.js")

    # swap whatever back-link it carries for the full app nav, or insert one
    html, n = re.subn(r'<a class="back-link"[^>]*>.*?</a>', NAV, html, count=1, flags=re.S)
    if not n:
        html, n = re.subn(r'(<div class="hero-inner">)',
                          r'\1\n    <div class="topnav">' + NAV + "</div>",
                          html, count=1)
        if not n:
            print("  warning: could not place the app nav")

    if "<footer>" in html:
        html = html.replace("<footer>", SECTIONS + "  <footer>", 1)
    else:
        print("  warning: no footer found; engagement sections not inserted")

    html = html.replace("</body>", SCRIPTS, 1)
    html = html.replace("</html>", MARK + "\n</html>", 1)

    open(PAGE, "w").write(html)
    print("patched sand-technologies-dashboard.html")


if __name__ == "__main__":
    main()
