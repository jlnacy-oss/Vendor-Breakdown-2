# GIP Vendor & Technology Tracker

A private static site tracking 49 vendors across frontier AI, enterprise software,
data platforms, industrial AI and systems integration — what they do, who we know
there, and where every GIP engagement stands.

Built September 2026, extending the Physical AI / Industrial AI market landscape.

---

**Two data layers, one rule:** market and person research is regenerable and holds only
public professional information. Anything personal — email, mobile, what you learned in
the room — lives only in `gip-tracker.xlsx`, entered by you. Run
`python3 scripts/upgrade_workbook.py` after pulling a new version to add any new columns
without touching your data.

**Open `TODO.txt` first** — it lists the decisions that gate the next build items,
what to populate, and which vendors to refresh before using externally.

## Running it

**Easiest:** double-click `start-windows.bat` (Windows) or `start-mac.command` (Mac).
That serves the folder at `http://localhost:8765` and opens it. Leave the window open
while you use the app; close it when you're done.

**Or open `index.html` directly.** Everything works except automatic loading of your
data — browsers block pages opened from disk from reading other files. Click
**Load tracker** and pick `gip-tracker.xlsx` instead. One extra click per session.

Nothing is uploaded, published or sent anywhere. There is no server beyond your own
machine and no network calls at all — SheetJS and Chart.js are bundled in the folder.

---

## The two data layers

This is the important idea. Keep them separate and nothing you type ever gets
overwritten by a refresh.

| Layer | File | Who maintains it | Regenerable? |
|---|---|---|---|
| Market / deep research | `scripts/research_data.py` → `app-data.js` | research passes | Yes — throw away and rebuild |
| GIP engagement data | `gip-tracker.xlsx` | you, by hand | **No — this is the original** |

The research layer knows what a vendor sells and who runs it. Your workbook knows
who asked for the intro, which PortCo it went to, and where it stands. The site joins
them in the browser at load time. A research refresh never touches your workbook.

**Back up `gip-tracker.xlsx`.** It is the only file here that can't be regenerated.

---

## Pages

| Page | What it does |
|---|---|
| `index.html` | All 49 vendors as cards. Filter by category, search, or show only vendors you're engaged with. Alphabetical index table below. |
| `tracker.html` | Every engagement thread — who requested, the connection, the reason, PortCo, use case, status, owner, next step. Filter by status or vendor. |
| `scorecard.html` | One score per vendor summarising engagement breadth, depth, momentum and substance. |
| `people.html` | Contact cards for every key person, seeded with researched executives and extended by your workbook. |
| `<vendor>-dashboard.html` | The white page for one vendor, ending in its GIP engagement block and contacts. |
| `person-<id>.html` | Full profile for one contact. |

---

## Working the workbook

Six sheets. Only ever edit `gip-tracker.xlsx`; the site reads it and never writes back.

- **Engagements** — one row per vendor / PortCo / use-case thread. A vendor can have
  many rows. This sheet drives the tracker page and the entire scorecard.
- **People** — contacts, seeded from the research layer (grey cells). The right-hand
  columns are yours, for what you pick up in the room and nothing else researches:
  **Mobile**, **Preferred Contact**, **Assistant / EA**, **Where We Met**,
  **Facts From Meetings**, **Next Touch**, **Next Touch Due** — alongside Work Email,
  Phone, LinkedIn, How We Know Them and Last Contact. All of it flows straight to that
  person's dashboard, and to their white paper in a `--with-notes` build.
- **Vendors** — relationship owner, tier, and the optional score override.
- **PortCos** — your portfolio list. Feeds the PortCo dropdown on Engagements.
- **Lists** — the dropdown values. Edit here to change what the dropdowns offer.
- **README** — the same guidance, inside the file.

Rules that keep it working: don't rename sheets or change row-1 headers; leave grey
reference cells alone (the slug and Person ID are how rows join to the white pages);
delete the yellow EXAMPLE rows once you have real data.

### How the score is calculated

Out of 100, from the Engagements rows — this measures **our engagement**, not vendor
quality. A great vendor scores zero if we haven't done anything with them.

- **Breadth (30)** — distinct PortCos introduced, capped at five
- **Depth (30)** — furthest status any thread has reached
- **Momentum (20)** — how recently anything moved (30 days or less earns full marks, decaying to zero past a year)
- **Substance (20)** — share of threads with a real use case written down

Put a number in **Score Override** on the Vendors sheet to replace the calculation
entirely, and say why in the next column. The scorecard shows the override and its
reason instead of the bars.

---

## Publishing to GitHub

The repo is safe to publish. `gip-tracker.xlsx` is listed in `.gitignore`, so your
engagement data is never committed and never appears on the public site.

```bash
cd <this folder>
git init
git add .
git commit -m "GIP vendor and technology tracker"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
```

Then in the repo: **Settings → Pages → Source: Deploy from a branch → main / (root)**.
The site appears at `https://<you>.github.io/<repo>/` within a minute or two.

**Check before you push.** `git status` should never list `gip-tracker.xlsx`. If it
does, the `.gitignore` isn't being picked up — stop and fix that first. A `.nojekyll`
file is included so GitHub Pages serves every file as-is.

**What the public site shows:** vendor research, categories, filters, contacts from the
research layer. The tracker, scorecard and engagement panels render empty with a
"Load tracker" prompt, because there is no workbook on the server. That is the intended
behaviour, not a bug.

**What you see locally:** the same site plus all your data, because the workbook sits
next to `index.html` on your machine.

If you later want the real data on a hosted site, that needs a private repo on a
GitHub Team plan (Pages from private repos is a paid feature) or internal hosting.

---

## Research status

**All 49 vendors now carry full deep-research white pages.** Every one has financials,
leadership, sourced use cases with links, competitive position, and customer / market /
employee sentiment.

Where a figure could not be confirmed it is left blank or shown as a range with the
uncertainty stated, rather than estimated. Several pages carry an explicit research note
flagging thin sourcing (Tribola Tech, NTT DATA, Syntax), figures that move quickly
(OpenAI, Databricks, Perplexity, Meta, Google), or details deliberately omitted because
they could not be verified (Adobe's CTO, Anthropic's CTO).

Research goes stale. Re-run a vendor before using any number externally.

### Waves

Research runs alphabetically, in waves. Vendor waves are complete; person waves are
tracked separately in `scripts/people_wave<N>.py` and are at 82 of 97.

| Wave | Date | Vendors |
|---|---|---|
| 0 | Sept 2026 | Sand Technologies, Palantir, C3.ai, Cognite, Bentley Systems, AVEVA, IBM watsonx, Honeywell Forge, Siemens Xcelerator |
| 1 | 15 Sept 2026 | Accenture, Adobe, Amazon Web Services |
| 2 | 15 Sept 2026 | Anthropic, Aziro, Bain & Company, Booz Allen Hamilton, Boston Consulting Group |
| 3 | 15 Sept 2026 | Capgemini, Cognizant, CrowdStrike, Databricks, Deloitte |
| 4 | 15 Sept 2026 | DXC Technology, EY, Google, HCLTech, IBM Consulting |
| 5 | 15 Sept 2026 | Infosys, KPMG, McKinsey & Company, Meta, Microsoft |
| 6 | 15 Sept 2026 | NTT DATA, NVIDIA, OpenAI, Oracle, Perplexity |
| 7 | 15 Sept 2026 | PwC, Salesforce, SAP, ServiceNow, Snowflake |
| 8 | 15 Sept 2026 | Syntax, TCS, Tribola Tech, UiPath, Wipro, Workday, xAI |

**Complete — all 49 vendors researched.** To refresh a vendor, edit its record in the
relevant `scripts/deep_wave<N>.py` and rebuild. To add a new vendor, add it to `PENDING`
in `scripts/research_data.py` (it will render as a research shell) and promote it into a
wave file once researched.

Each wave is its own module — `scripts/deep_wave1.py`, `deep_wave2.py` and so on —
aggregated by `scripts/deep_research.py`. A vendor with a completed pass is filtered
out of `PENDING` automatically and keeps its tags and group, so the filters don't shift.

The workbook's vendor list and seeded contacts are generated from the research layer,
which means a vendor name can never drift between the two and silently break the join
on the Vendor column.

After a wave lands, run `python3 scripts/sync_people.py` to add the newly researched
executives to your People sheet. It only appends — it never edits, reorders or deletes
anything you have typed.

---

## Rebuilding and regenerating

**Everything except `gip-tracker.xlsx` can be thrown away and rebuilt.** That is the
whole design. One command does it:

```bash
./rebuild.sh          # Mac / Linux
rebuild.bat           # Windows
```

That validates the research layer, then regenerates the overview, tracker, scorecard,
contacts page, all 49 white pages, all 92 person pages, all 49 vendor one-sheet PDFs and
all 92 contact one-sheet PDFs. It stops on a validation failure rather than publishing a
broken page. It never writes to your workbook except to *append* newly researched
contacts to the People sheet.

### Refreshing the market research

The research itself is regenerated by calling the Claude API with web search:

```bash
export ANTHROPIC_API_KEY=sk-ant-...            # Windows: set ANTHROPIC_API_KEY=...

python3 scripts/refresh_research.py oracle anthropic   # named vendors
python3 scripts/refresh_research.py --stale 90         # anything 90+ days old
python3 scripts/refresh_research.py --all              # everything (slow, expensive)
python3 scripts/refresh_research.py oracle --dry-run   # show the prompt, call nothing
./rebuild.sh                                           # then rebuild
```

Each refreshed record is **validated before it is written**. If Claude returns something
that does not match the schema — a missing field, a use case without a real source URL,
fewer than two use cases — the record is rejected and the previous one is left untouched.

Refreshed records land in `scripts/deep_refreshed.py`, which overrides the original wave
files by slug. So the eight `deep_wave<N>.py` files remain an audit trail of the original
research, and **a bad refresh is undone by deleting that vendor's entry from the overlay**.
A malformed overlay is ignored with a warning rather than breaking the site.

`refresh_research.py` never reads or writes `gip-tracker.xlsx`.

### Checking the research layer

```bash
python3 scripts/validate_research.py       # strict
python3 scripts/validate_research.py --lenient
```

Reports missing fields, sources that are not URLs, duplicate slugs, HTML entities in
vendor names (which would silently break the join to your workbook), and any vendor whose
research is more than 90 days old.

### Individual build steps

If you would rather run them one at a time:

| Command | Produces |
|---|---|
| `python3 scripts/build_site.py` | `app-data.js`, overview, tracker, scorecard, contacts, person pages |
| `python3 scripts/build_dashboards.py` | the 48 data-driven vendor white pages |
| `python3 scripts/patch_sand.py` | splices the app into Sand's hand-built page (idempotent) |
| `python3 scripts/build_pdfs.py` | 48 vendor one-sheet PDFs (add a slug to do just one) |
| `python3 scripts/build_sand_onesheet.py` | Sand's hand-built one-sheet |
| `python3 scripts/build_contact_sheets.py` | 92 contact white papers (PDF) |
| `python3 scripts/refresh_people.py --pending` | research the contacts not yet covered |
| `python3 scripts/sync_people.py` | appends newly researched contacts to your People sheet |
| `python3 scripts/upgrade_workbook.py` | adds any missing columns to your workbook, non-destructively |

### Refreshing the person research

Every contact gets a dashboard page and a downloadable white paper. The professional
research behind them is regenerated the same way:

```bash
python3 scripts/refresh_people.py --pending           # everyone not yet researched
python3 scripts/refresh_people.py --vendor oracle     # everyone at one vendor
python3 scripts/refresh_people.py palantir-alex-karp  # one person
python3 scripts/refresh_people.py --pending --limit 10
./rebuild.sh
```

**The privacy rule, and how it is enforced.** Person research holds professional,
published information only: role, career history, education, what they own today, public
board seats, published talks and articles, and links to those sources.

It never holds personal information — email, phone, home address or city, spouse,
children, family, date of birth, age, salary, net worth, health, religion or politics —
**even where a public source carries it**. Wikipedia and press profiles routinely publish
these; they are not needed to prepare for a business meeting and are not republished here.

This is enforced mechanically, not by habit. `people_schema.check_privacy()` scans every
record for banned fields, email addresses, phone numbers and personal phrasing. A record
that trips it is **rejected outright, not sanitised**, and the previous record stands. The
same check runs in `validate_research.py` on every build.

Personal contact details exist in exactly one place: the **People** sheet of
`gip-tracker.xlsx`, entered by you, from your own dealings. They appear on the person
dashboard and — only in a `--with-notes` build — on the white paper.

### Contact one-sheets

Every contact has a downloadable one-page meeting-prep sheet — who you're meeting, what
their company does, the key numbers, where it sits competitively, what to pressure-test,
and the GIP/BlackRock position. Linked from the contacts page, the person page and the
vendor white page.

```bash
python3 scripts/build_contact_sheets.py                    # public sheets
python3 scripts/build_contact_sheets.py --with-notes       # adds YOUR workbook data
python3 scripts/build_contact_sheets.py palantir-alex-karp # just one person
```

The default build contains research-layer material only and is safe to publish. The
`--with-notes` build additionally pulls email, phone, relationship owner, how you know
them and that vendor's live engagement threads out of `gip-tracker.xlsx`, and writes to
`private-contact-sheets/` — which is in `.gitignore` and marked confidential in the
document footer.

### The Sand Technologies exception

Sand's dashboard and PDF were hand-built before the data-driven pipeline existed and
carry more research depth than the generated pages. They are **not** produced from
`vendor_data.py`; editing that file will not change them. `patch_sand.py` splices in
the nav, styles and engagement blocks without disturbing the research content, and is
safe to re-run.

### Adding a vendor

Add a row to the **Vendors** sheet and it appears in the dropdowns immediately. To give
it a white page, add an entry to `PENDING` in `scripts/research_data.py` and rebuild.

---

## Files

```
index.html / market-overview.html   overview
tracker.html  scorecard.html  people.html
<slug>-dashboard.html               49 vendor white pages
person-<id>.html                    21 contact profiles
<slug>-one-sheet.pdf                9 downloadable one-pagers

gip-tracker.xlsx                    YOUR DATA — back this up
app-data.js                         generated research layer
gip-loader.js                       reads the workbook in the browser
gip-panel.js                        engagement block on vendor pages
xlsx.full.min.js  chart.umd.js      bundled libraries (no CDN, works offline)
start-windows.bat  start-mac.command

scripts/
  research_data.py    all 49 vendors + the filter taxonomy (regenerable)
  vendor_data.py      deep research for the original 9
  shared.css app.css  styles
  build_site.py  build_dashboards.py  build_pdfs.py
  build_overview.py   build_sand_onesheet.py  patch_sand.py
```

Everything must stay in one flat folder — all links between pages are relative.
