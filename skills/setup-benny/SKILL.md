---
name: setup-benny
description: "Prepare optional Benny issue-triage and reproduction recipes for Rakazo; create live jobs only when explicitly requested."
---

## Rakazo execution

On the first rstack skill used in this task, load `skill_read({"name":"rstack","file":"references/rakazo.md"})`. It defines native tools, resource loading, helper limits, model selection and authorization. This workflow does not grant extra permissions. References below are companion files retrieved with `skill_read`, not installed filesystem paths.

# Set up Benny

Benny is optional. Installing rstack installs these recipes and creates no live automation. Inspect the target repository, source channel, issue tracker, control adapter and available connector actions before asking for missing configuration.

Read templates/configuration.example.yaml and the feature-map/routing companions of the operational skills. Store completed, secret-free configuration at an agreed repository location, preserving existing user-owned files. Record the target bot and allowed actions. Use its current model by default; explicit overrides require a supported provider/model pair. A skill or file name in a template is a placeholder until a real available implementation is verified.

Keep triage and reproduction separate. Both must have source identity checks, duplicate handling, bounded effort, a safe test environment and an explicit outcome. Triage may post or write issues only when the user authorizes those actions. Reproduction may open draft PRs only when authorized. Helpers inherit the same scope and cannot delegate recursively.

Create or update jobs only when explicitly requested, using native schedule tools for supported triggers or the authenticated app for webhook-enabled routines. Use the live tool schema, inspect existing jobs, and verify saved prompts and triggers. If the desired source needs an unavailable integration, leave the proposed configuration reviewable and name the missing capability. Do not simulate a running event subscription with a hidden loop.

Test the two recipes against an authorized synthetic report with external writes disabled first. Then test only the explicitly authorized actions. Include stop conditions, resource budgets, artifact retention and cleanup in the deployed prompts.
