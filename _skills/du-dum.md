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
fetched_at: '2026-04-19T04:51:31.279396+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-19T06:36:03.381117Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7d0ca180 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7d0ca180 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-19T07:27:51.477739Z'
indexed_at: '2026-04-19T07:27:51.477745Z'
---
