---
name: rstack-help
description: "Browse the full rstack package and choose a workflow or principle for a concrete Rakazo task."
---

## Rakazo execution

On the first rstack skill used in this task, load `skill_read({"name":"rstack","file":"references/rakazo.md"})`. It defines native tools, resource loading, helper limits, model selection and authorization. This workflow does not grant extra permissions. References below are companion files retrieved with `skill_read`, not installed filesystem paths.

# Rstack help

Load `skill_read({"name":"rstack","file":"references/catalogue.json"})` for the complete installed inventory, source-name mappings and companion paths. For task routing, load `rstack-mode`. Use skill names in natural language, for example "use rstack to investigate this bug" or "use architect to compare these designs"; slash-command rendering depends on the client.

The original 58 skills and two helper roles are present. `interrogate` is named `rstack-interrogate` to coexist with Rakazo's built-in Interrogate. The routing, setup, help and delegate names use rstack. The three optional Benny automation recipes are also available, dormant. `rstack` is the package entry point.

Use setup-rstack for environment checks. Helpers inherit the bot's model; no particular AI provider is required. For a missing tool, explain which workflow is affected and use an available equivalent where it preserves the task. Do not pretend a missing source was searched.
