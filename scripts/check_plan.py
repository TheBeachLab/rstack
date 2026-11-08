#!/usr/bin/env python3
"""Check a bounded rstack phase plan without executing any commands."""
import json
import sys
from pathlib import Path


def check(plan):
    if not isinstance(plan, dict):
        raise ValueError("Plan must be an object")
    for key in ("goal", "scope", "stop_condition"):
        if not isinstance(plan.get(key), str) or not plan[key].strip():
            raise ValueError(f"A non-empty {key} is required")
    steps = plan.get("steps")
    if not isinstance(steps, list) or not steps:
        raise ValueError("At least one step is required")
    ids = set()
    for step in steps:
        if not isinstance(step, dict):
            raise ValueError("Each step must be an object")
        for key in ("id", "deliverable", "write_scope", "verification"):
            if not isinstance(step.get(key), str) or not step[key].strip():
                raise ValueError(f"Each step needs a non-empty {key}")
        if step["id"] in ids:
            raise ValueError(f"Duplicate step: {step['id']}")
        dependencies = step.get("depends_on", [])
        if not isinstance(dependencies, list) or any(not isinstance(d, str) or d not in ids for d in dependencies):
            raise ValueError(f"Dependencies must name earlier steps: {step['id']}")
        ids.add(step["id"])
    return len(steps)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 check_plan.py plan.json")
    try:
        count = check(json.loads(Path(sys.argv[1]).read_text()))
    except (ValueError, OSError) as error:
        sys.exit(str(error))
    print(f"Valid plan: {count} ordered, verifiable steps")
