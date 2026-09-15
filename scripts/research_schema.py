# -*- coding: utf-8 -*-
"""
research_schema.py — the contract every vendor research record must satisfy.

Used by:
  refresh_research.py   to tell Claude exactly what to produce, and to reject bad output
  validate_research.py  to check the whole research layer before a build

Keeping the schema in one place means a regenerated record cannot silently drift
from the shape the site expects.
"""

REQUIRED_TEXT = [
    "slug", "name", "website", "linkedin", "group", "category", "tagline",
    "founded", "hq", "employees", "ownership", "revenue", "revenue_short",
    "offering", "digital_twin", "genai", "buyer", "description", "position_note",
    "gip_connection", "blackrock_connection", "customer_sentiment", "employee_sentiment",
]
REQUIRED_LIST = ["customers", "people", "use_cases", "sentiment_bull", "sentiment_bear"]
OPTIONAL = ["kpis", "notes", "glassdoor", "has_pdf", "has_full_dashboard"]

USE_CASE_KEYS = ["sector", "status", "deployment", "impact", "source"]
PERSON_KEYS = ["name", "title"]

GROUPS = [
    "Physical / Industrial AI", "Frontier AI / LLM", "Enterprise software",
    "Data platform", "Automation", "Cybersecurity", "SI / Consulting",
]


def validate(v, strict=True):
    """Return a list of problems with a single vendor record. Empty means valid."""
    problems = []
    slug = v.get("slug", "<no slug>")

    for k in REQUIRED_TEXT:
        val = v.get(k)
        if not isinstance(val, str) or not val.strip():
            problems.append(f"{slug}: '{k}' missing or empty")
    for k in REQUIRED_LIST:
        if not isinstance(v.get(k), list):
            problems.append(f"{slug}: '{k}' must be a list")

    if "&amp;" in str(v.get("name", "")):
        problems.append(f"{slug}: 'name' contains an HTML entity — it must be plain text, "
                        "because it is matched against the Vendor column in gip-tracker.xlsx")

    if v.get("group") and v["group"] not in GROUPS:
        problems.append(f"{slug}: group '{v['group']}' is not one of {GROUPS}")

    for i, uc in enumerate(v.get("use_cases", []) or []):
        if not isinstance(uc, dict):
            problems.append(f"{slug}: use_cases[{i}] is not an object")
            continue
        for k in USE_CASE_KEYS:
            if not str(uc.get(k, "")).strip():
                problems.append(f"{slug}: use_cases[{i}].{k} missing")
        src = str(uc.get("source", ""))
        if src and not src.startswith("http"):
            problems.append(f"{slug}: use_cases[{i}].source is not a URL")

    for i, p in enumerate(v.get("people", []) or []):
        if not isinstance(p, dict):
            problems.append(f"{slug}: people[{i}] is not an object")
            continue
        for k in PERSON_KEYS:
            if not str(p.get(k, "")).strip():
                problems.append(f"{slug}: people[{i}].{k} missing")

    if strict:
        if len(v.get("use_cases", []) or []) < 2:
            problems.append(f"{slug}: fewer than 2 use cases — a thin page, re-run the research")
        if len(v.get("sentiment_bull", []) or []) < 3:
            problems.append(f"{slug}: fewer than 3 supporting points")
        if len(v.get("sentiment_bear", []) or []) < 3:
            problems.append(f"{slug}: fewer than 3 points to pressure-test")

    kpis = v.get("kpis")
    if kpis is not None:
        if not isinstance(kpis, list) or not (4 <= len(kpis) <= 5):
            problems.append(f"{slug}: 'kpis' must be a list of 4 or 5 (value, label) pairs")
        else:
            for i, pair in enumerate(kpis):
                if not (isinstance(pair, (list, tuple)) and len(pair) == 2):
                    problems.append(f"{slug}: kpis[{i}] is not a (value, label) pair")

    return problems


def validate_all(vendors, strict=True):
    problems, seen = [], {}
    for v in vendors:
        problems += validate(v, strict=strict)
        slug = v.get("slug")
        if slug in seen:
            problems.append(f"{slug}: duplicate slug")
        seen[slug] = True
    return problems
