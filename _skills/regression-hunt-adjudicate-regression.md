---
id: regression-hunt-adjudicate-regression
slug: regression-hunt-adjudicate-regression
name: Adjudicate evidence
description: '- “S0 passes and S1 fails”: exposing an existing defect is a latent
  bug.'
prompt_preview: '---

  name: adjudicate-regression

  description: Use when deciding whether source and live reproduction evidence establish
  a new regression or an exclusion.

  ---


  # Adjudicate evidence


  ## When to Use


  Input: candidate, frozen sources, available reproduction/replay packages and

  registry assignment. Use a fresh context distinct from the reproducer

  and replayer. Early exclusions may lack experiments.

  Follow [project guidance](../../references/evidence.md#project-guidance) before
  target work.


  ## When N...'
full_prompt_length: 2639
tools_mentioned: []
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/regression-hunt/skills/adjudicate-regression/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/regression-hunt/skills/adjudicate-regression/SKILL.md
fetched_at: '2026-10-25T07:20:38.532935+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:43:45.081069Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e32d100 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e32d100 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:08.977504Z'
indexed_at: '2026-10-25T12:12:08.977508Z'
---
