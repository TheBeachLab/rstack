---
name: recall
description: "Reconstruct a scoped working context from Rakazo chat history, connected records and current evidence."
---

## Rakazo execution

On the first rstack skill used in this task, load `skill_read({"name":"rstack","file":"references/rakazo.md"})`. It defines native tools, resource loading, helper limits, model selection and authorization. This workflow does not grant extra permissions. References below are companion files retrieved with `skill_read`, not installed filesystem paths.

# Recall

Pin the topic, bot/project and time window. Use the user's supplied state capsule when sufficient. For one specific handoff, load the session-pickup playbook.

Search native history with narrow queries, normally `scope: "this_chat"`. Cross-chat recall requested by the user can use `scope: "my_chats"` in the direct human chat. Read matching messages using their returned `messageId` and `threadId`, following pagination only as needed. Do this in the parent; pass minimum relevant excerpts to helpers rather than asking them to bypass history access.

For a named subsystem, use why's available source guidance to corroborate recent issues, decisions and fixes. Verify branches, PRs and runtime state before calling them complete. Distinguish inaccessible evidence from no matching results.

Return a tight current-state capsule, one status per workstream, material problems, and the next concrete action. Cite actual message/source identifiers. Keep unrelated private history out of the answer.
