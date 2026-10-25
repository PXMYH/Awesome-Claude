---
id: regression-hunt-prepare-regression
slug: regression-hunt-prepare-regression
name: Prepare a change
description: '- “The PR is merged”: that does not identify the complete change boundary.'
prompt_preview: '---

  name: prepare-regression

  description: Use when pinning before/after sources and collecting PR or commit context
  for a regression investigation.

  ---


  # Prepare a change


  ## When to Use


  Input: PR URL or repository plus commit/range, and registry assignment.

  Follow [project guidance](../../references/evidence.md#project-guidance) after resolving
  the target commit.


  ## When NOT to Use


  The same inputs have a verified preparation record; reuse it.


  ## Prepare


  1. Read the [standard](../../docs/r...'
full_prompt_length: 2055
tools_mentioned: []
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/regression-hunt/skills/prepare-regression/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/regression-hunt/skills/prepare-regression/SKILL.md
fetched_at: '2026-10-25T07:20:38.757658+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:44:01.277632Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8df1d550 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8df1d550 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:08.981891Z'
indexed_at: '2026-10-25T12:12:08.981895Z'
---
