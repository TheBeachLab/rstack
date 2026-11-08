---
name: automate-me
description: "Turn a demonstrated repeated workflow into a reusable Rakazo skill or an explicitly requested native schedule."
---

## Rakazo execution

On the first rstack skill used in this task, load `skill_read({"name":"rstack","file":"references/rakazo.md"})`. It defines native tools, resource loading, helper limits, model selection and authorization. This workflow does not grant extra permissions. References below are companion files retrieved with `skill_read`, not installed filesystem paths.

# Automate me

Clarify the repeated outcome from the request and scoped native history. Separate recurring structure from one-off details and preserve user/project boundaries. Identify inputs, outputs, tools, authorization, failure behavior and a concrete completion predicate.

Prefer a reusable native skill for on-demand work. Draft concise instructions with verified tools and references; use skill_create or skill_update when the user asked to create or change it. Exercise a representative safe case and a missing-input case before declaring it ready.

For an explicitly requested recurring job, inspect schedule_list for duplicates and the live schedule_create schema. Specify prompt, bot, timezone, trigger, budget, delivery destination and stop condition. Use only supported cron, interval, one-shot or watch triggers. Read back the created job. Do not create a recurring job to follow a single task already in progress.

External messages and tracker changes need explicit authorization in the task or approved automation instructions. Never turn historical behavior into permission. A proposed routine is not running until the native creation succeeds. For webhook input use make-bot-ui's native endpoint guidance, not a schedule trigger that does not exist.
