---
id: regression-hunt-replay-regression
slug: regression-hunt-replay-regression
name: Independently replay a PoC
description: '- “The previous logs look right”: replay requires your own execution.'
prompt_preview: '---

  name: replay-regression

  description: Use when independently verifying a supplied PoC against fresh live
  before/after deployments.

  ---


  # Independently replay a PoC


  ## When to Use


  Input: candidate, frozen source records, complete sealed reproduction package

  and registry assignment. Use a fresh context distinct from the reproducer.

  Follow [project guidance](../../references/evidence.md#project-guidance) before
  target work.


  ## When NOT to Use


  Authoring or repairing the PoC. Return changes t...'
full_prompt_length: 1999
tools_mentioned: []
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/regression-hunt/skills/replay-regression/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/regression-hunt/skills/replay-regression/SKILL.md
fetched_at: '2026-10-25T07:20:38.958390+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:44:17.489245Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e32ccb0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e32ccb0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:08.986209Z'
indexed_at: '2026-10-25T12:12:08.986213Z'
---
