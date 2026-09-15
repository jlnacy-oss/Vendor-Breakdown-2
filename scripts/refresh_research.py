# -*- coding: utf-8 -*-
"""
refresh_research.py — regenerate the market-research layer for one or more vendors.

    export ANTHROPIC_API_KEY=sk-ant-...
    python3 scripts/refresh_research.py anthropic oracle       # named vendors
    python3 scripts/refresh_research.py --stale 90             # anything researched 90+ days ago
    python3 scripts/refresh_research.py --all                  # everything (slow, expensive)
    python3 scripts/refresh_research.py anthropic --dry-run    # show the prompt, call nothing

How it works
------------
For each vendor, this calls the Claude API with the web search tool and asks for a
single JSON object matching research_schema.py. The result is validated before it is
written. Refreshed records land in scripts/deep_refreshed.py, which deep_research.py
overlays on top of the original wave files by slug — so the waves stay as an audit
trail of what was researched when, and a bad refresh can be undone by deleting the
overlay entry.

NOTHING in this script touches gip-tracker.xlsx. The GIP layer is never regenerated.
"""
import argparse
import datetime as dt
import json
import pprint
import os
import re
import sys
import urllib.error
import urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from research_schema import GROUPS, validate

API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-sonnet-4-6"
OVERLAY = os.path.join(SCRIPT_DIR, "deep_refreshed.py")

SYSTEM = """You are researching enterprise technology vendors for an infrastructure \
private-equity firm's internal vendor tracker. Your output is read by a Managing Director \
who will act on it, so accuracy matters more than completeness.

Rules you must follow:
1. Search the web. Do not answer from memory — figures move quarterly.
2. Prefer primary sources: company press releases, investor relations pages, SEC filings, \
annual reports. Use secondary sources only where no primary source exists, and say so.
3. Every use case must carry a real, working source URL that you actually retrieved.
4. If you cannot confirm something, leave the field explicitly vague ("Not disclosed", \
"Not confirmed in this pass") rather than estimating. Never invent a number, a person, \
or a customer name.
5. Where widely-quoted figures conflict, say so in the text and give the range.
6. The 'sentiment_bear' list is the honest case against the vendor. Write it as if the \
reader is about to spend money — include declining metrics, governance issues, litigation, \
concentration risk and disclosure gaps. Do not soften it.
7. Do not invent any relationship between the vendor and GIP or BlackRock. If none is \
publicly disclosed, say that plainly.

Return ONE JSON object and nothing else. No markdown fences, no preamble."""

FIELD_GUIDE = """Return JSON with exactly these keys:

slug              (string) keep the slug you were given, unchanged
name              (string) legal/common name, PLAIN TEXT — no HTML entities, no "&amp;"
website           (string) primary URL
linkedin          (string) company LinkedIn URL
group             (string) one of: %s
category          (string) short category label, e.g. "Cloud infrastructure & AI platform"
tagline           (string) one line, under 140 chars, what makes this vendor distinctive
founded           (string) year plus context if useful
hq                (string) headquarters
employees         (string) headcount with date, or "Not disclosed"
ownership         (string) public/private, ticker, parent, recent ownership events
revenue           (string) latest reported revenue with period and growth; note conflicts
revenue_short     (string) very short form for tables, e.g. "$21.1B (2025)"
offering          (string) 2-4 sentences on what they actually sell
digital_twin      (string) short: "Yes", "No", "Via partners", etc.
genai             (string) short: "Yes (product name)" or similar
buyer             (string) who buys it
customers         (array of strings) named public customers only, [] if none confirmed
people            (array of {name, title}) CEO and CTO at minimum where confirmable.
                  OMIT a person entirely rather than guessing their role.
description       (string) 2-3 sentences, the headline story with the key numbers
position_note     (string) 4-8 sentences: where this vendor sits, what is genuinely
                  differentiated, and what an infrastructure PE owner should watch
gip_connection    (string) any publicly disclosed GIP relationship, or state plainly
                  that none is disclosed, plus how it would most plausibly arise
blackrock_connection (string) same, for BlackRock
use_cases         (array of 4 objects) each {sector, status, deployment, impact, source}
                  status is one of: Deployed, Announced, Research finding
                  source MUST be a URL you retrieved
customer_sentiment   (string) what the evidence says about customers, incl. weaknesses
sentiment_bull    (array of 4 strings) what genuinely supports the story
sentiment_bear    (array of 5 strings) the honest case against — be specific and blunt
employee_sentiment   (string) workforce signals, or state it was not covered
kpis              (array of exactly 5 [value, label] pairs) short strings for the header
notes             (string, optional) research caveats: thin sourcing, fast-moving figures,
                  fields deliberately left out. Omit the key if there are none.
""" % ", ".join(GROUPS)


def call_claude(prompt, api_key, max_searches=12):
    body = {
        "model": MODEL,
        "max_tokens": 8000,
        "system": SYSTEM,
        "messages": [{"role": "user", "content": prompt}],
        "tools": [{"type": "web_search_20250305", "name": "web_search",
                   "max_uses": max_searches}],
    }
    req = urllib.request.Request(
        API_URL, data=json.dumps(body).encode("utf-8"),
        headers={"content-type": "application/json",
                 "x-api-key": api_key,
                 "anthropic-version": "2023-06-01"})
    with urllib.request.urlopen(req, timeout=600) as r:
        data = json.loads(r.read().decode("utf-8"))
    return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")


def extract_json(text):
    text = text.strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.M).strip()
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < 0:
        raise ValueError("no JSON object found in the response")
    return json.loads(text[start:end + 1])


def load_overlay():
    if not os.path.exists(OVERLAY):
        return {}
    ns = {}
    exec(compile(open(OVERLAY).read(), OVERLAY, "exec"), ns)
    return {v["slug"]: v for v in ns.get("VENDORS", [])}


def write_overlay(records):
    header = '''# -*- coding: utf-8 -*-
"""
deep_refreshed.py — GENERATED. Do not edit by hand.

Records here override the original wave files by slug. Written by
refresh_research.py; delete an entry to fall back to the wave version.
Last written: %s
"""

VENDORS = ''' % dt.date.today().isoformat()
    ordered = [records[k] for k in sorted(records)]
    # This file is imported as Python, so it must hold Python literals — JSON's
    # null/true/false would raise NameError on import. pprint emits None/True/False.
    body = pprint.pformat(ordered, indent=1, width=100, sort_dicts=False)
    with open(OVERLAY, "w") as f:
        f.write(header + body + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*", help="vendor slugs to refresh")
    ap.add_argument("--all", action="store_true", help="refresh every vendor")
    ap.add_argument("--stale", type=int, metavar="DAYS",
                    help="refresh vendors whose record is at least DAYS old")
    ap.add_argument("--dry-run", action="store_true", help="print the prompt, call nothing")
    args = ap.parse_args()

    from deep_research import DEEP, refreshed_on
    index = {v["slug"]: v for v in DEEP}

    if args.all:
        targets = sorted(index)
    elif args.stale is not None:
        cutoff = dt.date.today() - dt.timedelta(days=args.stale)
        targets = sorted(s for s in index
                         if refreshed_on(s) is None or refreshed_on(s) <= cutoff)
    else:
        targets = args.slugs
    if not targets:
        ap.error("name at least one vendor slug, or use --all / --stale N")

    unknown = [s for s in targets if s not in index]
    if unknown:
        ap.error("unknown slug(s): " + ", ".join(unknown)
                 + "\nknown slugs: " + ", ".join(sorted(index)))

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key and not args.dry_run:
        print("ANTHROPIC_API_KEY is not set.\n"
              "  export ANTHROPIC_API_KEY=sk-ant-...\n"
              "Or run with --dry-run to see the prompt without calling the API.")
        return 1

    overlay = load_overlay()
    ok, failed = [], []

    for slug in targets:
        current = index[slug]
        prompt = (
            f"Research the vendor '{current['name']}' (slug: {slug}, website: "
            f"{current['website']}) and return an updated record.\n\n"
            f"Today's date is {dt.date.today().strftime('%d %B %Y')}. Find the most recent "
            f"reported financials, current leadership, and material developments.\n\n"
            f"For reference, the previous record described them as: "
            f"\"{current.get('description', '')[:400]}\"\n"
            f"Do not assume any of that is still true — verify everything.\n\n"
            + FIELD_GUIDE)

        if args.dry_run:
            print("=" * 70)
            print(f"WOULD REFRESH: {slug}")
            print("=" * 70)
            print(prompt[:1400] + "\n[...]\n")
            continue

        print(f"refreshing {slug} ...", flush=True)
        try:
            raw = call_claude(prompt, api_key)
            rec = extract_json(raw)
            rec["slug"] = slug
            rec.setdefault("group", current.get("group"))
            rec["refreshed_on"] = dt.date.today().isoformat()
            problems = validate(rec)
            if problems:
                print("  rejected — record did not validate:")
                for p in problems[:8]:
                    print("    -", p)
                failed.append(slug)
                continue
            overlay[slug] = rec
            ok.append(slug)
            print(f"  ok ({len(rec.get('use_cases', []))} use cases)")
        except urllib.error.HTTPError as e:
            print(f"  API error {e.code}: {e.read().decode('utf-8', 'replace')[:300]}")
            failed.append(slug)
        except Exception as e:
            print(f"  failed: {e}")
            failed.append(slug)

    if args.dry_run:
        return 0

    if ok:
        write_overlay(overlay)
        print(f"\nwrote {len(ok)} record(s) to scripts/deep_refreshed.py")
        print("now rebuild:  ./rebuild.sh")
    if failed:
        print(f"\n{len(failed)} vendor(s) failed and were left unchanged: {', '.join(failed)}")
    return 1 if failed and not ok else 0


if __name__ == "__main__":
    sys.exit(main())
