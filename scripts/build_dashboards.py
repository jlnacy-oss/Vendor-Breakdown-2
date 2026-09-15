# -*- coding: utf-8 -*-
import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)
from vendor_data import VENDORS as _CORE
from deep_research import DEEP

for _v in _CORE:
    _v.setdefault("group", "Physical / Industrial AI")
VENDORS = _CORE + DEEP

# tags live in the research index; attach them so the competitive table can
# widen beyond a thin group
from research_data import BY_SLUG as _IDX
for _v in VENDORS:
    _v.setdefault("tags", _IDX.get(_v["slug"], {}).get("tags", []))

SHARED_CSS = (open(os.path.join(SCRIPT_DIR, 'shared.css')).read()
              + open(os.path.join(SCRIPT_DIR, 'app.css')).read())

def chip_row(items):
    return "".join(f'<span class="chip">{c}</span>' for c in items)

def uc_card(uc):
    return f"""
      <a class="uc-card" href="{uc['source']}" target="_blank" rel="noopener">
        <div class="uc-top"><span class="uc-sector">{uc['sector']}</span><span class="uc-status">{uc['status']}</span></div>
        <div class="uc-deploy">{uc['deployment']}</div>
        <div class="uc-metric">{uc['impact']}</div>
        <div class="uc-src">Source ↗</div>
      </a>"""

def people_chip_row(people):
    return "".join(f'<span class="chip"><b>{p["name"]}</b> — {p["title"]}</span>' for p in people)

def comp_table_rows(self_slug, group=None, tags=None):
    """Peers within the same group; if that group has fewer than three other
    tracked vendors, widen to anyone sharing a category tag so the table is
    still worth reading."""
    from research_data import VENDORS as ALL_TRACKED

    def row(v):
        dash = f"{v['slug']}-dashboard.html"
        label = v["category"] if len(v["category"]) < 60 else " \u00b7 ".join(v.get("tags", [])[:3])
        return (f'<tr><td class="mname"><a href="{dash}">{v["name"]}</a></td>'
                f'<td>{label}</td><td>{v["revenue_short"]}</td></tr>')

    others = [v for v in ALL_TRACKED if v["slug"] != self_slug]
    peers = [v for v in others if group and v.get("group") == group]
    if len(peers) < 3 and tags:
        seen = {v["slug"] for v in peers}
        for v in others:
            if v["slug"] in seen:
                continue
            if set(v.get("tags", [])) & set(tags):
                peers.append(v)
                seen.add(v["slug"])
    if not peers:
        peers = others
    peers.sort(key=lambda v: v["name"].lower())
    return "".join(row(v) for v in peers)


def bull_list(items):
    return "".join(f"<li>{b}</li>" for b in items)

def bear_list(items):
    return "".join(f"<li>{b}</li>" for b in items)

def vendor_page(v):
    pdf_name = "Sand-Technologies-One-Sheet.pdf" if v['slug'] == 'sand-technologies' else f"{v['slug']}-one-sheet.pdf"
    gd = v.get("glassdoor")

    if v.get("kpis"):
        kpi_html = "".join(
            f'<div class="kpi"><div class="num">{n}</div><div class="lbl">{l}</div></div>'
            for n, l in v["kpis"])
    else:
        _own = ('Public' if 'Public' in v['ownership']
                else ('Subsidiary' if 'ubsidiary' in v['ownership'] or 'Product line' in v['ownership']
                      or 'Platform of' in v['ownership']
                      else ('Acquired' if 'cquir' in v['ownership'] else 'Private')))
        kpi_html = (
            f'<div class="kpi"><div class="num">{__import__("re").search(r"[0-9]{4}", v["founded"]).group()}</div><div class="lbl">Founded</div></div>'
            f'<div class="kpi"><div class="num">{v["employees"].split(" ")[0]}</div><div class="lbl">Employees</div></div>'
            f'<div class="kpi"><div class="num">{v["revenue_short"]}</div><div class="lbl">Latest reported / estimated revenue</div></div>'
            f'<div class="kpi"><div class="num">{_own}</div><div class="lbl">Ownership</div></div>'
            + (f'<div class="kpi"><div class="num">{gd["rating"]} / 5</div><div class="lbl">Glassdoor rating ({gd["reviews"]} reviews)</div></div>' if gd else ''))

    _peers = comp_table_rows(v['slug'], v.get('group'), v.get('tags'))
    _npeers = _peers.count("<tr>")
    thin_note = ('<div class="sec-note" style="margin-top:12px;">Only '
                 f'{_npeers} directly comparable vendor{"" if _npeers == 1 else "s"} '
                 'is currently tracked in this app, so this table understates the real competitive '
                 'field. See <b>Where it sits</b> below for the wider market position.'
                 '</div>') if _npeers < 3 else ''

    pdf_btn = (f'<a class="btn" href="{pdf_name}" download>Download one-pager (PDF) &darr;</a>'
               if v.get("has_pdf", True) else '')
    notes_html = (f'<div class="callout" style="margin-top:18px;"><b>Research note:</b> {v["notes"]}</div>'
                  if v.get("notes") else '')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{v['name']} — Vendor Profile</title>
<style>
{SHARED_CSS}
</style>
</head>
<body>

<header class="hero">
  <div class="hero-inner">
    <div class="topnav">
      <a class="back-link" href="index.html">&larr; All vendors</a>
      &nbsp;&nbsp;<a class="back-link" href="tracker.html">Engagement tracker</a>
      &nbsp;&nbsp;<a class="back-link" href="scorecard.html">Scorecard</a>
      &nbsp;&nbsp;<a class="back-link" href="people.html">All contacts</a>
    </div>
    <div class="kicker"><span class="dot"></span>VENDOR PROFILE &nbsp;\u00b7&nbsp; {v['category'].upper()} &nbsp;\u00b7&nbsp; SEPTEMBER 11, 2026</div>
    <h1><a href="{v['website']}" target="_blank" rel="noopener" style="color:inherit; text-decoration:none;">{v['name']} \u2197</a></h1>
    <p class="tagline">{v['tagline']}</p>
    <div class="kpi-row">{kpi_html}</div>
    <div class="btn-row">
      {pdf_btn}
      <a class="btn secondary" href="{v['website']}" target="_blank" rel="noopener">Visit website ↗</a>
      <a class="btn secondary" href="market-overview.html">← All vendors in this market</a>
    </div>
  </div>
</header>

<div class="wrap">

  <section>
    <div class="sec-head"><span class="sec-num">01</span><h2>Company snapshot</h2></div>
    <div class="snap-grid">
      <div>
        <p>{v['description']}</p>
        <p><b>Offering:</b> {v['offering']}</p>
        {notes_html}
      </div>
      <div>
        <div class="side-block">
          <h4>Key facts</h4>
          <p style="margin:0 0 6px;"><b>Founded:</b> {v['founded']}</p>
          <p style="margin:0 0 6px;"><b>HQ:</b> {v['hq']}</p>
          <p style="margin:0 0 6px;"><b>Ownership:</b> {v['ownership']}</p>
          <p style="margin:0 0 6px;"><b>Revenue:</b> {v['revenue']}</p>
          <p style="margin:0;"><b>Web:</b> <a href="{v['website']}" target="_blank" rel="noopener" style="color:var(--steel);">{v['website'].replace('https://','')}</a> &nbsp;\u00b7&nbsp; <a href="{v['linkedin']}" target="_blank" rel="noopener" style="color:var(--steel);">LinkedIn ↗</a></p>
        </div>
        <div class="side-block">
          <h4>Key people</h4>
          <div class="chip-row">{people_chip_row(v['people'])}</div>
        </div>
        <div class="side-block">
          <h4>Named customers (public sources)</h4>
          <div class="chip-row">{chip_row(v['customers'])}</div>
        </div>
        <div class="side-block">
          <h4>Capabilities</h4>
          <div class="grade-row">
            <div class="grade"><div class="letter" style="font-size:13px;">{v['digital_twin'].split('(')[0].strip()}</div><div class="cap">Digital twin</div></div>
            <div class="grade"><div class="letter" style="font-size:13px;">{v['genai'].split('(')[0].strip()}</div><div class="cap">Agentic / GenAI</div></div>
          </div>
          <div style="margin-top:10px;" class="qual-note">Primary buyer: {v['buyer']}</div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="sec-head"><span class="sec-num">02</span><h2>Use cases &amp; reported metrics</h2></div>
    <div class="sec-note">All impact figures below are vendor- or partner-reported and have not been independently audited.</div>
    <div class="uc-grid">{"".join(uc_card(uc) for uc in v['use_cases'])}
    </div>
  </section>

  <section>
    <div class="sec-head"><span class="sec-num">03</span><h2>Competitive landscape</h2></div>
    <table class="comp-table">
      <thead><tr><th style="width:28%;">Vendor</th><th style="width:44%;">Category</th><th>Revenue (latest/est.)</th></tr></thead>
      <tbody>{_peers}
      </tbody>
    </table>
    {thin_note}
    <div class="position-note"><b>Where it sits:</b> {v['position_note']}</div>
  </section>

  <section>
    <div class="sec-head"><span class="sec-num">04</span><h2>GIP &amp; BlackRock connections</h2></div>
    <div class="sec-note">Global Infrastructure Partners (GIP) became a wholly-owned BlackRock subsidiary in October 2024 and now operates as BlackRock's dedicated infrastructure-investment arm. Ownership stakes below are standard institutional/index-fund positions unless otherwise noted \u2014 that is a capital-markets fact, not evidence of an operating relationship.</div>
    <table class="scale-table">
      <thead><tr><th style="width:22%;">Entity</th><th>Possible connection</th></tr></thead>
      <tbody>
        <tr><td class="name">Global Infrastructure Partners</td><td>{v['gip_connection']}</td></tr>
        <tr><td class="name">BlackRock</td><td>{v['blackrock_connection']}</td></tr>
      </tbody>
    </table>
  </section>

  <section>
    <div class="sec-head"><span class="sec-num">05</span><h2>Sentiment</h2></div>

    <div class="subhead">Customer sentiment</div>
    <div class="qual-note" style="margin-bottom:18px;">{v['customer_sentiment']}</div>

    <div class="subhead">Market &amp; analyst sentiment</div>
    <div class="sent-grid">
      <div class="sent-col bull">
        <div class="sent-head">What supports the story</div>
        <ul>{bull_list(v['sentiment_bull'])}</ul>
      </div>
      <div class="sent-col bear">
        <div class="sent-head">What to pressure-test</div>
        <ul>{bear_list(v['sentiment_bear'])}</ul>
      </div>
    </div>

    <div class="subhead">Employee sentiment</div>
    <div class="qual-note">{v['employee_sentiment']}</div>
  </section>

  <section>
    <div class="sec-head"><span class="sec-num">06</span><h2>GIP engagement</h2></div>
    <div class="sec-note">Live from your tracker workbook. Nothing here is published or uploaded.</div>
    <div id="gip-loadbar" class="loadbar">Reading gip-tracker.xlsx\u2026</div>
    <div class="gip-panel" id="gip-panel" data-vendor="{v['name']}"></div>
  </section>

  <section>
    <div class="sec-head"><span class="sec-num">07</span><h2>Contacts</h2></div>
    <div class="sec-note">Each card opens that person's dashboard, which links to their downloadable
    white paper. <a href="people.html?vendor={v['slug']}" style="color:var(--steel);">All {v['name']} contacts &rarr;</a>
    &nbsp;\u00b7&nbsp; <a href="people.html" style="color:var(--steel);">All contacts across every vendor &rarr;</a></div>
    <div class="card-grid" id="gip-people"></div>
    <div id="nopeople" class="empty" style="display:none;"><b>No contacts on file</b>Add rows for {v['name']} on the People sheet.</div>
  </section>

  <footer>
    <b>Sources:</b> {v['name']} public filings/website, company fact sheets, Wikipedia, PitchBook/Crunchbase/Datanyze/BuiltIn company profiles, Glassdoor employer reviews, vendor case studies and press releases, SEC Schedule 13D/13G/13F filings, and BlackRock/GIP corporate disclosures, as of September 2026. Figures marked \u201cest.\u201d or \u201cnot disclosed\u201d are third-party estimates or unavailable, not company-confirmed \u2014 validate in diligence.<br>
    Part of the <a href="market-overview.html" style="color:var(--steel);">Physical AI / Industrial AI for Critical Infrastructure market landscape</a>.
  </footer>

</div>
<script src="xlsx.full.min.js"></script>
<script src="gip-loader.js"></script>
<script src="app-data.js"></script>
<script src="gip-panel.js"></script>
</body>
</html>
"""
    return html

if __name__ == "__main__":
    for v in VENDORS:
        if v.get("has_full_dashboard"):
            continue  # Sand keeps its existing deep-dive dashboard
        out_path = os.path.join(ROOT_DIR, f"{v['slug']}-dashboard.html")
        with open(out_path, "w") as f:
            f.write(vendor_page(v))
        print("wrote", out_path)
