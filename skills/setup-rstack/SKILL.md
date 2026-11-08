---
name: setup-rstack
description: "Check that rstack skills and required Rakazo tools are available; configure only user-requested workflow preferences."
---

## Rakazo execution

On the first rstack skill used in this task, load `skill_read({"name":"rstack","file":"references/rakazo.md"})`. It defines native tools, resource loading, helper limits, model selection and authorization. This workflow does not grant extra permissions. References below are companion files retrieved with `skill_read`, not installed filesystem paths.

# Set up rstack

1. Load `rstack-mode` and the catalogue companion. Check the required tools for the requested workflow against the live tool list.
2. Inspect the bot computer and relevant repository instructions. Identify connected evidence sources with `task_catalog` only when needed.
3. Use the bot's existing model for main work and helpers. A different provider/model pair is optional and must already be available; this skill does not buy access, alter global model settings or ask for a new API key.
4. Preserve existing preferences. If the user requests durable per-role preferences, store only supported provider/model pairs and scope in the project's established configuration or bot instructions through an available authorized interface. There is no hidden editor model-rule file.
5. Check representative loads with `skill_read`, including a companion. Report missing capabilities for the affected workflow. Loading recipes does not create automations or webhooks.
