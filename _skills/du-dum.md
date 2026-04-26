---
id: du-dum
slug: du-dum
name: 'Du-Dum: Batch-Then-Act Pattern'
description: '- `manage-token-budget` -- cost control framework that du-dum makes
  practical; du-dum is the architectural pattern, token budget is the accounting layer'
prompt_preview: "---\nname: du-dum\ndescription: >\n  Separate expensive observation\
  \ from cheap decision-making in autonomous agent\n  loops using a two-clock architecture.\
  \ A fast clock accumulates data into a\n  digest file; a slow clock reads the digest\
  \ and acts only when something is\n  pending. Idle cycles cost nothing because the\
  \ action clock returns immediately\n  after reading an empty digest. Use when building\
  \ autonomous agents that must\n  observe continuously but can only afford to act\
  \ occasionally, when API o..."
full_prompt_length: 13389
tools_mentioned: []
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/du-dum/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/du-dum/SKILL.md
fetched_at: '2026-04-26T05:00:08.619042+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-26T06:49:59.120914Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe111f25a0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7efe111f25a0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-26T07:41:26.725626Z'
indexed_at: '2026-04-26T07:41:26.725631Z'
---
