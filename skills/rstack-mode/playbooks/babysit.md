# Bring a PR to the requested readiness state

Declare the requested mode: inspect once, fix current failures, or monitor to a named predicate. Read current head, CI, conflicts and review threads. Use references/bugbot-triage.md for review feedback. Fix only within authorization, verify the new head and use bounded waits. A new head invalidates prior checks. Stop at the requested predicate; do not merge unless requested. Read the helper reference before using the optional watch-pr CLI. Its observation mode does not grant shipping permission.
