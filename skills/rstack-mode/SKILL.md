---
name: rstack-mode
description: "Select and run the appropriate rstack engineering workflow in Rakazo, with native helpers and verifiable completion."
---

## Rakazo execution

On the first rstack skill used in this task, load `skill_read({"name":"rstack","file":"references/rakazo.md"})`. It defines native tools, resource loading, helper limits, model selection and authorization. This workflow does not grant extra permissions. References below are companion files retrieved with `skill_read`, not installed filesystem paths.

# Rstack mode

Match the user's task to a playbook below and load it with `skill_read({"name":"rstack-mode","file":"playbooks/<name>.md"})`. For multi-step work, track its concrete deliverables in the scratchpad. Apply only relevant principles through their leaf skills; a short task does not need every workflow.

- `investigation`: Answer a read-only question.
- `bug-fix`: Reproduce and fix a defect.
- `feature`: Implement changed behavior.
- `refactoring`: Change structure while preserving behavior.
- `perf-issue`: Improve a measured performance problem.
- `hillclimb`: Improve one metric through experiments.
- `runtime-forensics`: Diagnose a live runtime symptom.
- `trace-forensics`: Diagnose a captured profiling artifact.
- `prototype`: Build a bounded experiment to settle a choice.
- `visual-parity`: Verify visual equivalence.
- `authoring-a-skill`: Create or update a reusable skill.
- `eval`: Evaluate a skill or prompt change.
- `babysit`: Bring a PR to the requested readiness state.
- `shipping`: Land a verified change or stack.
- `autonomous-run`: Complete a bounded task in this conversation.
- `orchestrate`: Coordinate a project across bounded work units.
- `autopilot-full`: Build and land an explicitly authorized queue.
- `autopilot-stack`: Build a verified queue for later landing.
- `session-pickup`: Resume prior work.
- `pause-safely`: Pause on the user's request.
- `multi-phase-plan`: Plan and execute verifiable phases.
- `worktree-cleanup`: Reclaim only proven-unused worktrees.
- `opening-a-pr`: Prepare a reviewable pull request.

For code understanding use `how`; for motivation use `why`; for design use `architect` and `arena`; for adversarial review use `rstack-interrogate`; for broad coverage use `swarm`. Use `tdd` when a regression test is practical, `benchmark-checklist` before interpreting measurements, `statechart` for checked TLA+ diagrams, and `show-me-your-work` for a decision trail. Use `technical-writing` or `unslop` for their specific writing tasks. If no playbook fits, use `figure-it-out`.

No additional provider or model is required. The current bot's configured model is the default for every helper. The parent reviews helper evidence, owns edits and integration, and reports results in the user's language.
