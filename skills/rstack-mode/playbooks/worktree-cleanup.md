# Reclaim only proven-unused worktrees

Start with git worktree list, branch ancestry, tracked/untracked/ignored files and evidence of active use. Preserve current, primary, shared and protected-target checkouts. Retire only clean integrated inactive worktrees with no unique ignored files, using the repository's validated mechanism. Remove from outside the checkout with git worktree remove, then git branch -d. Never force or bypass hooks. Simulator cleanup needs separate evidence of ownership and authorization; do not treat it as implied by Git cleanup.
