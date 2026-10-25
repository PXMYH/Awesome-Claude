---
id: setup
slug: setup
name: ax:setup
description: '- Experiment-loop workflow → use `ax:retro`.'
prompt_preview: '---

  name: setup

  description: Install + verify ax (the agent experience layer). Triggers when the
  user says "install ax", "set up ax", "ax not found", "ax doctor", "is ax running",
  "fix ax install", "first-time ax setup", or any setup question about the ax CLI
  / skills / daemon. Walks the install via the install.sh + skills.sh + first ingest,
  validates with `ax doctor`, and points the user at ax:retro (experiment loop) and
  ax:extract-workflow (reconstruct workflow behind shipped artifacts).

  ---...'
full_prompt_length: 7846
tools_mentioned:
- TypeScript
category: community
category_display: Community
source_repo: Necmttn/ax
source_path: skills/setup/SKILL.md
source_url: https://github.com/Necmttn/ax/blob/main/skills/setup/SKILL.md
fetched_at: '2026-10-25T07:16:07.640242+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T08:02:40.199565Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8deb80e0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8deb80e0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:05.023767Z'
indexed_at: '2026-10-25T12:12:05.023771Z'
---
