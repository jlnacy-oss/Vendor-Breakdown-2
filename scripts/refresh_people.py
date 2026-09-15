# -*- coding: utf-8 -*-
"""
refresh_people.py — research or re-research the people behind each vendor.

    export ANTHROPIC_API_KEY=sk-ant-...
    python3 scripts/refresh_people.py --pending          # everyone not yet researched
    python3 scripts/refresh_people.py --vendor oracle    # everyone at one vendor
    python3 scripts/refresh_people.py palantir-alex-karp # one person
    python3 scripts/refresh_people.py --pending --limit 10
    python3 scripts/refresh_people.py --vendor sap --dry-run

PRIVACY. The prompt forbids personal information, and every returned record is put
through people_schema.check_privacy() before it is written. A record containing an
email address, phone number, home location, family detail, date of birth, salary or
net worth is REJECTED, not sanitised. Personal contact details belong only in the
People sheet of gip-tracker.xlsx, entered by you.

Results land in scripts/people_refreshed.py, which overrides the wave files by id.
"""
import argparse
import datetime as dt
import json
import os
import pprint
import re
import sys
import urllib.error
import urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from people_schema import check_privacy, validate
from research_data import VENDORS, person_id
import people_research

API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-sonnet-4-6"
OVERLAY = os.path.join(SCRIPT_DIR, "people_refreshed.py")

SYSTEM = """You are preparing professional briefing notes on named business executives for an \
infrastructure private-equity firm's internal vendor tracker. The reader is a Managing \
Director preparing for a meeting.

ABSOLUTE PRIVACY RULE — this overrides everything else:
Include ONLY professional, published information: current role, career history, education, \
what they are accountable for, public board seats and appointments, published talks, \
interviews and articles, and links to those sources.

NEVER include, even if a public source carries it: email addresses, phone numbers, home \
address or home city, where they live, spouse, partner, children, parents or any family \
detail, date of birth or age, salary, compensation or net worth, health, religion, \
ethnicity, or political affiliation. Wikipedia and press profiles frequently publish these. \
Leave them out anyway. They are not needed to prepare for a business meeting.

Other rules:
1. Search the web. Do not answer from memory.
2. Prefer the company's own leadership page, official announcements and reputable press.
3. If you cannot confirm something, omit it. Never invent a role, a date or a credential.
4. Talking points must be your own derived observations for a business meeting — not \
quotations attributed to the person.

Return ONE JSON object and nothing else. No markdown fences, no preamble."""

FIELD_GUIDE = """Return JSON with exactly these keys:

id             (string) keep the id you were given, unchanged
vendor_slug    (string) keep unchanged
name           (string) full name
title          (string) current role title
in_role_since  (string, optional) when they took the role, plus succession context if relevant
focus          (string) 1-2 sentences: what they are accountable for today
background     (string) 3-6 sentences: the career story and what it implies about how they think
career         (array of {period, role, org}) most recent first, 3-7 entries
education      (array of strings) e.g. "MBA, Kellogg School of Management". [] if unconfirmed.
public_roles   (array of strings) board seats, external appointments, notable recognition. [] if none.
notable        (array of 2-3 objects {point, source}) sourced, professionally relevant facts.
               'source' MUST be a URL you actually retrieved.
talking_points (array of 3 strings) your own observations for someone preparing to meet them
links          (array of {label, url}) 2-4 source links: company bio, LinkedIn, interviews, articles
notes          (string, optional) research caveats. Omit the key if there are none.

Do NOT include any key not listed above."""


def call_claude(prompt, api_key, max_searches=6):
    body = {"model": MODEL, "max_tokens": 4000, "system": SYSTEM,
            "messages": [{"role": "user", "content": prompt}],
            "tools": [{"type": "web_search_20250305", "name": "web_search",
                       "max_uses": max_searches}]}
    req = urllib.request.Request(
        API_URL, data=json.dumps(body).encode("utf-8"),
        headers={"content-type": "application/json", "x-api-key": api_key,
                 "anthropic-version": "2023-06-01"})
    with urllib.request.urlopen(req, timeout=420) as r:
        data = json.loads(r.read().decode("utf-8"))
    return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")


def extract_json(text):
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    a, b = text.find("{"), text.rfind("}")
    if a < 0 or b < 0:
        raise ValueError("no JSON object in the response")
    return json.loads(text[a:b + 1])


def load_overlay():
    if not os.path.exists(OVERLAY):
        return {}
    ns = {}
    exec(compile(open(OVERLAY).read(), OVERLAY, "exec"), ns)
    return {p["id"]: p for p in ns.get("PEOPLE", [])}


def write_overlay(records):
    header = '''# -*- coding: utf-8 -*-
"""
people_refreshed.py — GENERATED. Do not edit by hand.

Person records here override the wave files by id. Written by refresh_people.py;
delete an entry to fall back to the wave version. Every record was checked against
people_schema.check_privacy() before it was written.
Last written: %s
"""

PEOPLE = ''' % dt.date.today().isoformat()
    body = pprint.pformat([records[k] for k in sorted(records)], indent=1, width=100, sort_dicts=False)
    with open(OVERLAY, "w") as f:
        f.write(header + body + "\n")


def all_contacts():
    out = []
    for v in VENDORS:
        for p in v["people"]:
            out.append({"id": person_id(v["slug"], p["name"]), "vendor_slug": v["slug"],
                        "vendor": v["name"], "name": p["name"],
                        "title": p["title"].replace("&amp;", "&"),
                        "website": v["website"], "linkedin": v.get("linkedin", "")})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*", help="person ids to research")
    ap.add_argument("--vendor", help="every contact at this vendor slug")
    ap.add_argument("--pending", action="store_true", help="every contact not yet researched")
    ap.add_argument("--limit", type=int, help="stop after N people")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    contacts = {c["id"]: c for c in all_contacts()}
    done = set(people_research.BY_ID)

    if args.pending:
        targets = sorted(i for i in contacts if i not in done)
    elif args.vendor:
        targets = sorted(i for i, c in contacts.items() if c["vendor_slug"] == args.vendor)
        if not targets:
            ap.error(f"no contacts at vendor '{args.vendor}'")
    else:
        targets = args.ids
    if not targets:
        ap.error("name at least one person id, or use --vendor SLUG / --pending")

    unknown = [t for t in targets if t not in contacts]
    if unknown:
        ap.error("unknown person id(s): " + ", ".join(unknown))
    if args.limit:
        targets = targets[:args.limit]

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key and not args.dry_run:
        print("ANTHROPIC_API_KEY is not set. Export it, or use --dry-run.")
        return 1

    overlay = load_overlay()
    ok, failed, blocked = [], [], []

    for pid in targets:
        c = contacts[pid]
        prompt = (f"Research {c['name']}, {c['title']} at {c['vendor']} ({c['website']}).\n"
                  f"Person id: {pid}. Vendor slug: {c['vendor_slug']}.\n"
                  f"Today's date is {dt.date.today().strftime('%d %B %Y')}. Confirm they still hold "
                  f"this role; if they have moved on, say so in 'notes'.\n\n" + FIELD_GUIDE)
        if args.dry_run:
            print(f"WOULD RESEARCH: {pid} ({c['name']}, {c['vendor']})")
            continue

        print(f"researching {pid} ...", flush=True)
        try:
            rec = extract_json(call_claude(prompt, api_key))
            rec["id"], rec["vendor_slug"] = pid, c["vendor_slug"]
            rec["researched_on"] = dt.date.today().isoformat()

            privacy = check_privacy(rec)
            if privacy:
                print("  BLOCKED — the record contained personal information:")
                for x in privacy[:6]:
                    print("    -", x)
                blocked.append(pid)
                continue
            problems = validate(rec)
            if problems:
                print("  rejected — did not validate:")
                for x in problems[:6]:
                    print("    -", x)
                failed.append(pid)
                continue
            overlay[pid] = rec
            ok.append(pid)
            print(f"  ok ({len(rec.get('career', []))} career entries, "
                  f"{len(rec.get('links', []))} links)")
        except urllib.error.HTTPError as e:
            print(f"  API error {e.code}: {e.read().decode('utf-8', 'replace')[:200]}")
            failed.append(pid)
        except Exception as e:
            print(f"  failed: {e}")
            failed.append(pid)

    if args.dry_run:
        print(f"\n{len(targets)} person/people would be researched")
        return 0
    if ok:
        write_overlay(overlay)
        print(f"\nwrote {len(ok)} record(s) to scripts/people_refreshed.py")
        print("now rebuild:  ./rebuild.sh")
    if blocked:
        print(f"\n{len(blocked)} BLOCKED on privacy and not written: {', '.join(blocked)}")
    if failed:
        print(f"{len(failed)} failed and were left unchanged: {', '.join(failed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
