---
name: principle-never-block-on-the-human
description: "Apply when tempted to ask 'should I do X?' on reversible work."
---

## Rakazo execution

On the first rstack skill used in this task, load `skill_read({"name":"rstack","file":"references/rakazo.md"})`. It defines native tools, resource loading, helper limits, model selection and authorization. This workflow does not grant extra permissions. References below are companion files retrieved with `skill_read`, not installed filesystem paths.

# Never Block on the Human

The human supervises asynchronously. Agents should make progress within the user's authorization. Make reasonable decisions, proceed, and let the human course-correct after the fact. Since code changes are reversible and reviewable, a wrong decision usually costs less than blocking.

- Proceed, then present. Do the work, show the result. Don't ask "should I do X?" Do the authorized work and explain why.
- Make the system self-healing. Fix in-scope problems; report unrelated findings without silently expanding the task.
- Irreversible actions (force-push, delete production data, send external messages) require authorization for that action; do not ask again if it was already granted.
- Reversible actions (write code, edit notes, split tasks) should proceed when within the requested scope.
- Product direction comes from the human. Execution should not block.
