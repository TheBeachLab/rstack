# Plan and execute verifiable phases

Define end-to-end acceptance and dependency order. Give each phase one observable deliverable, owned write surface, validation and integration condition. Keep separately useful units small. Use show-me-your-work when the tradeoffs need an audit trail. Review shared interfaces before fan-out, enforce at most four helpers, and integrate only verified outputs. Replan from new evidence instead of preserving a stale checklist.

For a machine-checked plan, load `skill_read({"name":"rstack-mode","file":"references/plan.example.json"})`. Obtain the rstack source checkout for the installed release and run `python3 scripts/check_plan.py plan.json`. This replaces the upstream editor-specific plan checker.
