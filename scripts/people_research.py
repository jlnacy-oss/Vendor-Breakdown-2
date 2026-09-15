# -*- coding: utf-8 -*-
"""
people_research.py — aggregates every person-research wave, plus any refreshes.

Person records hold PROFESSIONAL, PUBLISHED information only. See people_schema.py
for the rule and the guard that enforces it on every write. Personal contact details
live only in the People sheet of gip-tracker.xlsx, entered by the user, and are never
researched.

people_refreshed.py, if present, is written by refresh_people.py and OVERRIDES wave
records by person id, exactly as deep_refreshed.py does for vendors.
"""
import datetime as _dt
import importlib

WAVE_MODULES = ["people_wave1", "people_wave2", "people_wave3", "people_wave4", "people_wave5", "people_wave6", "people_wave7", "people_wave8", "people_wave9", "people_wave10", "people_wave11", "people_wave12", "people_wave13", "people_wave14", "people_wave15", "people_wave16"]

WAVES, _base = [], []
for _name in WAVE_MODULES:
    try:
        _m = importlib.import_module(_name)
    except ImportError:
        continue
    _date = getattr(_m, "RESEARCHED_ON", "2026-09-15")
    WAVES.append((_name, _date, _m.PEOPLE))
    _base.extend(_m.PEOPLE)

RESEARCHED_ON = {}
for _n, _d, _people in WAVES:
    for _p in _people:
        RESEARCHED_ON[_p["id"]] = _p.get("researched_on", _d)

try:
    import people_refreshed
    _overlay = {p["id"]: p for p in people_refreshed.PEOPLE}
except ImportError:
    _overlay = {}
except Exception as _e:
    import warnings
    warnings.warn(f"scripts/people_refreshed.py could not be loaded and was ignored: {_e}")
    _overlay = {}

PEOPLE = []
for _p in _base:
    _pid = _p["id"]
    if _pid in _overlay:
        _r = _overlay[_pid]
        RESEARCHED_ON[_pid] = _r.get("researched_on", RESEARCHED_ON[_pid])
        PEOPLE.append(_r)
    else:
        PEOPLE.append(_p)

BY_ID = {p["id"]: p for p in PEOPLE}


def get(person_id):
    """Research record for a person id, or None if not yet researched."""
    return BY_ID.get(person_id)


def researched_on(person_id):
    raw = RESEARCHED_ON.get(person_id)
    if not raw:
        return None
    try:
        return _dt.date.fromisoformat(raw)
    except ValueError:
        return None


if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from research_data import VENDORS, person_id
    total = sum(len(v["people"]) for v in VENDORS)
    print(f"{len(PEOPLE)} of {total} contacts researched")
    done = {p["id"] for p in PEOPLE}
    pending = [person_id(v["slug"], p["name"]) for v in VENDORS for p in v["people"]
               if person_id(v["slug"], p["name"]) not in done]
    print(f"{len(pending)} pending, next alphabetically: " + ", ".join(sorted(pending)[:6]))
