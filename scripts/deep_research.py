# -*- coding: utf-8 -*-
"""
deep_research.py — aggregates every completed research wave, plus any refreshes.

Each wave lives in its own module (deep_wave1.py … deep_wave8.py) holding full-depth
vendor records in the same schema as vendor_data.py: financials, leadership, sourced
use cases with links, competitive position, and customer / market / employee sentiment.

scripts/deep_refreshed.py, if present, is written by refresh_research.py and OVERRIDES
wave records by slug. The wave files are therefore an audit trail of the original pass,
and a bad refresh is undone by deleting its entry from the overlay.

All of this is regenerable market research. No GIP-confidential data belongs here —
that lives only in gip-tracker.xlsx.
"""
import datetime as _dt

import deep_wave1
import deep_wave2
import deep_wave3
import deep_wave4
import deep_wave5
import deep_wave6
import deep_wave7
import deep_wave8

WAVES = [
    ("Wave 1", "2026-09-15", deep_wave1.VENDORS),
    ("Wave 2", "2026-09-15", deep_wave2.VENDORS),
    ("Wave 3", "2026-09-15", deep_wave3.VENDORS),
    ("Wave 4", "2026-09-15", deep_wave4.VENDORS),
    ("Wave 5", "2026-09-15", deep_wave5.VENDORS),
    ("Wave 6", "2026-09-15", deep_wave6.VENDORS),
    ("Wave 7", "2026-09-15", deep_wave7.VENDORS),
    ("Wave 8", "2026-09-15", deep_wave8.VENDORS),
]

# date each vendor's record was last produced, by slug
RESEARCHED_ON = {}
_base = []
for _name, _date, _vendors in WAVES:
    for _v in _vendors:
        RESEARCHED_ON[_v["slug"]] = _date
        _base.append(_v)

# refreshes override the original wave record for that slug
try:
    import deep_refreshed
    _overlay = {v["slug"]: v for v in deep_refreshed.VENDORS}
except ImportError:
    _overlay = {}
except Exception as _e:  # a broken overlay must never take the whole app down
    import warnings
    warnings.warn(f"scripts/deep_refreshed.py could not be loaded and was ignored: {_e}. "
                  "Delete it to clear this, then re-run the refresh.")
    _overlay = {}

DEEP = []
for _v in _base:
    _slug = _v["slug"]
    if _slug in _overlay:
        _r = _overlay[_slug]
        RESEARCHED_ON[_slug] = _r.get("refreshed_on", RESEARCHED_ON[_slug])
        DEEP.append(_r)
    else:
        DEEP.append(_v)


def refreshed_on(slug):
    """Date this vendor's research was last produced, or None."""
    raw = RESEARCHED_ON.get(slug)
    if not raw:
        return None
    try:
        return _dt.date.fromisoformat(raw)
    except ValueError:
        return None


def stale(days=90, today=None):
    """Slugs whose research is at least `days` old."""
    today = today or _dt.date.today()
    cutoff = today - _dt.timedelta(days=days)
    return sorted(s for s in RESEARCHED_ON
                  if refreshed_on(s) is None or refreshed_on(s) <= cutoff)


if __name__ == "__main__":
    for name, date, vendors in WAVES:
        print(f"{name} ({date}): " + ", ".join(v["name"] for v in vendors))
    print(f"\n{len(DEEP)} vendors with deep research"
          + (f"; {len(_overlay)} refreshed" if _overlay else ""))
