---
id: skeptical-triage
slug: skeptical-triage
name: Skeptical Triage
description: '- **Don''t triage P2/advisory findings.** The whole point is gate decisions.
  P2 is advisory — let the author see it and move on.'
prompt_preview: "---\nname: skeptical-triage\ndescription: Reusable 3-round self-challenge\
  \ + arbiter pattern for filtering false positives from findings/verdicts. Use when\
  \ the cost of a false-positive gate block exceeds the cost of ~4 extra LLM turns.\n\
  when_to_use: |\n  Apply skeptical triage when:\n  - A finding could block a gate\
  \ (gate:code, gate:ship, gate:qa, gate:arch) and flipping it wrongly wastes CTO\
  \ time\n  - A verdict is about to be written to a report that downstream agents\
  \ will trust (CSO, QA, ADR)\n  - Mul..."
full_prompt_length: 8404
tools_mentioned: []
category: community
category_display: Community
source_repo: avelikiy/great_cto
source_path: skills/skeptical-triage/SKILL.md
source_url: https://github.com/avelikiy/great_cto/blob/main/skills/skeptical-triage/SKILL.md
fetched_at: '2026-07-19T05:20:43.008151+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T06:25:13.333877Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101c35f0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101c35f0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:18.092960Z'
indexed_at: '2026-07-19T09:13:18.092966Z'
---
