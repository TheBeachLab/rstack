---
name: rstack
description: "Rakazo-native engineering workflows: start a coding, debugging, investigation or review task; use rstack-help to browse the full package."
---

## Rakazo execution

On the first rstack skill used in this task, load `skill_read({"name":"rstack","file":"references/rakazo.md"})`. It defines native tools, resource loading, helper limits, model selection and authorization. This workflow does not grant extra permissions. References below are companion files retrieved with `skill_read`, not installed filesystem paths.

# Rstack

Use `skill_read({"name":"rstack-mode"})` to select a workflow for the requested task. Use `rstack-help` for the catalogue and `setup-rstack` for environment checks. Load only the workflow and references needed now.

This package ports every skill and helper role from pstack 0.15.36 to Rakazo. Its optional Benny recipes remain dormant until a user explicitly requests automation setup. Installing skills does not create schedules, webhooks, bots, model subscriptions or credentials.
