# rstack

The full [pstack](https://github.com/cursor/plugins/tree/c742dd61706fbacc1b95f1a20b7b988cf096ce6c/pstack) engineering workflow package, adapted for Rakazo.

**64 skills:** all 58 upstream skills, both helper roles, three optional Benny automation recipes, and the `rstack` entry point. Includes coding, debugging, architecture, adversarial review, performance measurement, formal verification, technical writing and handoffs.

## Install in Rakazo

Open Rakazo's Skills manager and use its plugin import option with:

```text
https://github.com/TheBeachLab/rstack
```

Preview the package and install its skills. It uses the generic Agent Plugins manifest supported by Rakazo. No MCP connector or new model key is required. Avoid installing the original pstack alongside it: most workflow names intentionally stay the same and would collide.

Ask your bot: **“Use rstack to investigate this bug”**, **“Use rstack-help”**, or **“Use setup-rstack to check this environment.”** Names also work through `skill_read`; slash-command presentation depends on your client.

## What changed

- Helpers use Rakazo's native `run_subagent`, inherit the current bot model, run in batches of at most four and do not nest.
- History uses native `search_history` and `read_history`, respecting chat access.
- References load through `skill_read`, including workflows that the original importer skipped because they contained scripts.
- Scheduling and webhook recipes use Rakazo's interfaces. Installation creates no jobs, webhooks, bots or external messages.
- The original `interrogate` becomes `rstack-interrogate`, preserving Rakazo's built-in Interrogate. `poteto-mode`, `poteto-help`, `poteto-agent` and `setup-pstack` become `rstack-mode`, `rstack-help`, `rstack-agent` and `setup-rstack`.
- Editor model rules, transcript paths, background-agent flags and forced cleanup instructions are replaced with native workflows. Playbooks respect the user's authorization and the repository's integration rules.

The [catalogue](skills/rstack/references/catalogue.json) lists every skill and resource. [Upstream provenance](upstream.json) records the exact source revision and per-skill hashes.

## Optional helpers and prerequisites

Rakazo installs text instructions and references, not executable files. Statechart/TLC, decision logging and PR observation use **optional, pinned upstream helpers fetched when needed**. See the [helper instructions](skills/rstack/references/helpers.md). Formal checking needs a suitable TypeScript runtime and Java/TLC; diagram image rendering has an additional renderer dependency. A skill being installed does not mean these dependencies are installed or every workflow has been executed.

The native plan validator is available from a checkout of this repository:

```sh
python3 scripts/check_plan.py plan.json
```

Use the [plan example](skills/rstack-mode/references/plan.example.json) as the shape, replacing it with the actual task. The checker validates ordered dependencies, write scopes, verification and a stopping condition. It executes no plan steps.

Benny requires a configured source channel, tracker, safe test environment, control adapter and explicit permission for its external actions. Its recipes remain dormant until configured.

## Validation

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

The validator checks complete coverage, names, companion references, importer size/type limits and known incompatible editor instructions. The package is also checked with Rakazo's native plugin parser and skill loader before release. These are compatibility checks, not a claim that all workflows have been exercised against every provider, application or connector.

## Attribution

Adapted from **pstack 0.15.36 by Lauren Tan**, pinned to [`c742dd6`](https://github.com/cursor/plugins/tree/c742dd61706fbacc1b95f1a20b7b988cf096ce6c/pstack). MIT licensed; the original copyright and licence are preserved. Adaptation by TheBeachLab. This is an independent project, not an official Cursor or Rakazo release.
