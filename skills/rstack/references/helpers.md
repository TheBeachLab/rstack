# Optional executable helpers

The full upstream executable source, tests and fixtures remain available at the pinned public source. Rakazo imports text references, so scripts are fetched on demand instead of being silently skipped as part of a skill.

- Repository: https://github.com/cursor/plugins
- Commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`
- Required subtree: `pstack`

In an isolated working directory with git available, clone the public repository using sparse checkout, fetch/check out the exact commit and compare `git rev-parse HEAD` with the pin before execution. Do not execute a moving branch, pipe a network response to a shell, or reuse a dirty checkout. A possible sequence, with a new chosen destination, is:

```sh
git clone --filter=blob:none --no-checkout https://github.com/cursor/plugins.git rstack-upstream
git -C rstack-upstream sparse-checkout set pstack
git -C rstack-upstream checkout --detach c742dd61706fbacc1b95f1a20b7b988cf096ce6c
git -C rstack-upstream rev-parse HEAD
```

Run only the helper needed for the user's task, after inspecting its source, dependency manifest and available runtime:

| Workflow | Path below the verified checkout | Requirements |
| --- | --- | --- |
| Checked state diagrams | `pstack/skills/statechart/scripts/statechart` | TypeScript-capable Node/Bun/Deno; Java/TLC through the helper's mise bootstrap |
| Decision log | `pstack/skills/show-me-your-work/scripts/log.sh` | POSIX shell; escapes spreadsheet-formula cells |
| Plan-shape validation | `scripts/check_plan.py` in the installed rstack release checkout | Python 3; see the plan example in rstack-mode |
| Bounded PR observation | `pstack/skills/poteto-mode/scripts/watch-pr/watch-pr` | Bun, authenticated gh and dependencies from its package manifest |

Use native rstack-mode instructions for runtime setup and worktree cleanup; the upstream editor bootstrap, editor-specific plan checker and transcript-based worktree audit are replaced by these native workflows. Do not execute those editor-specific helpers. A watcher can observe checks, but it does not grant permission to merge or publish. Inspect its help and select a bounded observation mode; stop it when the requested predicate is reached.

Inspect the helper's own tests for fixtures and usage. Do not count fetching source as having run a check. If prerequisites cannot be provided in scope, return the useful model/log/plan and the exact unrun step. Diagram rendering is optional and separately documented by statechart's render reference.
