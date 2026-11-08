---
name: comment-sicko
description: "Review scoped comments and suppressions for redundancy or hidden design problems; return evidence-backed deletion and refactoring suggestions."
---

## Rakazo execution

On the first rstack skill used in this task, load `skill_read({"name":"rstack","file":"references/rakazo.md"})`. It defines native tools, resource loading, helper limits, model selection and authorization. This workflow does not grant extra permissions. References below are companion files retrieved with `skill_read`, not installed filesystem paths.

# Comment review helper

Read the scoped diff and nearby code. Work read-only unless comment edits were explicitly delegated. Preserve legal/license notices, public API contracts and evidence-backed external constraints. Identify narration, dead commented code and explanations that could be expressed more clearly in names, types or structure.

For a lint/type suppression, inspect the actual rule and behavior before suggesting removal. Preserve a needed safeguard until the underlying code can be corrected and verified. Use how or why for uncertain context without nested helpers. Doubt is a reason to investigate, not evidence for deletion.

Return file/line, the proposed deletion or rewrite, reason, required verification and any separately scoped refactoring idea. The parent owns application-code changes and the final reviewed patch.
