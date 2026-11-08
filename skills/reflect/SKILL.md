---
name: reflect
description: "Review the current Rakazo conversation for durable lessons and propose or apply specifically authorized skill improvements."
---

## Rakazo execution

On the first rstack skill used in this task, load `skill_read({"name":"rstack","file":"references/rakazo.md"})`. It defines native tools, resource loading, helper limits, model selection and authorization. This workflow does not grant extra permissions. References below are companion files retrieved with `skill_read`, not installed filesystem paths.

# Reflect

Use the current conversation and narrowly scoped native history. If full history is unavailable, state the evidence limit and use an accurate digest. Load the judgment, tooling and divergent reviewer prompts from this skill's references. Pass each the same scoped evidence; use at most three read-only native helpers or explicit sequential review passes.

Use references/synthesizer.md to combine verified findings into Accepted, Rejected and Backlog. Prefer a structural fix over another instruction when it prevents the repeated mistake. Route only to skills/tools actually used.

A request to reflect authorizes analysis. A request to apply the resulting changes authorizes scoped implementation. For edits not yet authorized, show the exact target and patch before asking. User-owned native skills can be changed with skill_update; plugin skills require source changes and reinstallation. Do not silently create duplicates, edit plugin caches, file tickets or send messages. Backlog is a local finding until external filing is explicitly authorized.

Validate changed skills and report actual edits with paths or native skill identities. Use the author's real integration workflow.
