# -*- coding: utf-8 -*-
"""
people_schema.py — the contract for a person research record, and the privacy
guard that every record must pass before it can be written.

THE RULE
--------
The research layer holds PROFESSIONAL, PUBLISHED information only: role, career
history, education, what they own today, public board seats and appointments,
published talks, interviews and articles, and links to those sources.

It must NEVER hold personal information, even where a public source carries it.
Wikipedia and press profiles routinely publish birth dates, spouses, children,
parents, home cities, net worth and salary. None of that belongs here. It is not
needed to prepare for a business meeting and it is not ours to republish.

Personal contact details — email, phone — exist in exactly one place: the People
sheet of gip-tracker.xlsx, entered by you, from your own dealings. They are never
researched, never written here, and never leave your machine.

check_privacy() below enforces this mechanically so the rule survives every future
refresh, not just the first one.
"""
import re

REQUIRED_TEXT = ["id", "vendor_slug", "name", "title", "focus", "background"]
REQUIRED_LIST = ["career", "education", "public_roles", "notable", "talking_points", "links"]
OPTIONAL = ["in_role_since", "researched_on", "notes"]

# Keys that must never appear in a person record, whatever the source said.
BANNED_KEYS = {
    "email", "e_mail", "mail", "phone", "mobile", "cell", "telephone", "fax",
    "address", "home", "home_town", "hometown", "residence", "lives_in", "based",
    "location", "city", "birth", "birthday", "birth_date", "dob", "born", "age",
    "spouse", "partner", "married", "marital_status", "children", "kids", "family",
    "parents", "father", "mother", "siblings", "relatives",
    "salary", "compensation", "pay", "net_worth", "wealth", "assets",
    "religion", "ethnicity", "race", "nationality", "sexual_orientation", "gender",
    "health", "medical", "disability", "politics", "political_affiliation",
    "personal_email", "direct_line", "handle", "personal",
}

# Patterns that suggest personal data leaked into free text.
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
PHONE_RE = re.compile(r"(?:\+\d[\d ().-]{8,}\d)|(?:\(\d{3}\)\s?\d{3}[- ]?\d{4})|(?:\b\d{3}[-.]\d{3}[-.]\d{4}\b)")
# Matched as whole words/phrases, not substrings. An earlier version matched
# "aged " inside "managed" and "leveraged", which flagged clean records.
PERSONAL_PHRASES = [
    r"his wife", r"her husband", r"his husband", r"her wife", r"\bspouse\b",
    r"married to", r"his children", r"her children", r"his son\b", r"her son\b",
    r"his daughter", r"her daughter", r"\blives in\b", r"\blives with\b",
    r"\bresides in\b", r"was born in", r"born in (?:19|20)\d\d",
    r"net worth", r"his salary", r"her salary", r"\bhome in\b",
    r"his family", r"her family", r"\baged \d\d\b",
    r"\b(?:he|she) is \d\d\b", r"\bdate of birth\b", r"\bcaste\b",
]


def check_privacy(rec):
    """Return a list of privacy violations. Empty means the record is clean."""
    problems = []
    who = rec.get("id") or rec.get("name") or "<unknown person>"

    for key in rec:
        if key.lower() in BANNED_KEYS:
            problems.append(f"{who}: field '{key}' is personal information and must not be stored here")

    def scan(text, where):
        t = str(text)
        if EMAIL_RE.search(t):
            problems.append(f"{who}: {where} contains an email address")
        if PHONE_RE.search(t):
            problems.append(f"{who}: {where} contains a phone number")
        low = t.lower()
        hits = []
        for phrase in PERSONAL_PHRASES:
            m = re.search(phrase, low)
            if m:
                hits.append(m.group(0))
        if hits:
            problems.append(f"{who}: {where} contains personal detail "
                            f"({', '.join(sorted(set(hits))[:4])})")

    def walk(value, where):
        if isinstance(value, str):
            scan(value, where)
        elif isinstance(value, dict):
            for k, v in value.items():
                walk(v, f"{where}.{k}")
        elif isinstance(value, (list, tuple)):
            for i, v in enumerate(value):
                walk(v, f"{where}[{i}]")

    for k, v in rec.items():
        if k == "links":
            continue  # URLs legitimately contain names and @ in some paths
        walk(v, k)

    return problems


def validate(rec, strict=True):
    """Structural validation. Always run check_privacy() alongside this."""
    problems = []
    who = rec.get("id", "<no id>")

    for k in REQUIRED_TEXT:
        if not isinstance(rec.get(k), str) or not rec[k].strip():
            problems.append(f"{who}: '{k}' missing or empty")
    for k in REQUIRED_LIST:
        if not isinstance(rec.get(k), list):
            problems.append(f"{who}: '{k}' must be a list")

    for i, c in enumerate(rec.get("career", []) or []):
        if not isinstance(c, dict) or not c.get("role") or not c.get("org"):
            problems.append(f"{who}: career[{i}] needs at least 'role' and 'org'")

    for i, n in enumerate(rec.get("notable", []) or []):
        if not isinstance(n, dict) or not n.get("point"):
            problems.append(f"{who}: notable[{i}] needs a 'point'")
        elif n.get("source") and not str(n["source"]).startswith("http"):
            problems.append(f"{who}: notable[{i}].source is not a URL")

    for i, l in enumerate(rec.get("links", []) or []):
        if not isinstance(l, dict) or not l.get("label") or not str(l.get("url", "")).startswith("http"):
            problems.append(f"{who}: links[{i}] needs a 'label' and an http(s) 'url'")

    if strict:
        if len(rec.get("career", []) or []) < 2:
            problems.append(f"{who}: fewer than 2 career entries — thin, re-run the research")
        if len(rec.get("links", []) or []) < 1:
            problems.append(f"{who}: no source links")

    return problems


def validate_all(records, strict=True):
    problems, seen = [], set()
    for r in records:
        problems += validate(r, strict=strict)
        problems += check_privacy(r)
        if r.get("id") in seen:
            problems.append(f"{r.get('id')}: duplicate person id")
        seen.add(r.get("id"))
    return problems
