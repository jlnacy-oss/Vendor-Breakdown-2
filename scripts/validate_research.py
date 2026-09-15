# -*- coding: utf-8 -*-
"""
validate_research.py — check the whole research layer before a build.

    python3 scripts/validate_research.py          # strict (fails on thin records)
    python3 scripts/validate_research.py --lenient

Run this after any refresh. rebuild.sh runs it automatically and stops on failure,
so a bad regeneration cannot quietly ship a broken or half-empty white page.
"""
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from research_schema import validate_all
from people_schema import validate_all as validate_people
from deep_research import DEEP, RESEARCHED_ON, stale
import people_research
from vendor_data import VENDORS as CORE
from research_data import VENDORS as INDEX


def main():
    strict = "--lenient" not in sys.argv
    problems = validate_all(DEEP, strict=strict)

    # the original nine predate the schema and legitimately lack some fields
    problems += [p for p in validate_all(CORE, strict=False)
                 if "'group'" not in p and "'kpis'" not in p]

    # every vendor in the index must resolve to a white page and a stable slug
    slugs = {v["slug"] for v in DEEP} | {v["slug"] for v in CORE}
    for v in INDEX:
        if v["slug"] not in slugs:
            problems.append(f"{v['slug']}: in the index but has no research record")
        if "&amp;" in v["name"]:
            problems.append(f"{v['slug']}: index name contains an HTML entity")

    # people research: structural checks plus the privacy guard
    ppl = people_research.PEOPLE
    problems += validate_people(ppl, strict=strict)
    known_ids = {person["id"] for v in INDEX for person in
                 [{"id": __import__("research_data").person_id(v["slug"], pp["name"])} for pp in v["people"]]}
    for r in ppl:
        if r["id"] not in known_ids:
            problems.append(f"{r['id']}: person record has no matching contact in the vendor index")

    total_people = sum(len(v["people"]) for v in INDEX)
    print(f"checked {len(INDEX)} vendors ({len(DEEP)} deep records) and "
          f"{len(ppl)} of {total_people} contacts, {'strict' if strict else 'lenient'} mode")
    if len(ppl) < total_people:
        print(f"  {total_people - len(ppl)} contact(s) not yet researched "
              f"(they render as 'Research pending')")

    old = stale(90)
    if old:
        print(f"\n{len(old)} vendor(s) researched more than 90 days ago:")
        print("  " + ", ".join(old[:12]) + (" ..." if len(old) > 12 else ""))
        print("  refresh with: python3 scripts/refresh_research.py --stale 90")

    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print("\nresearch layer is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
