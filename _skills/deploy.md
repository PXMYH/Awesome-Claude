---
id: deploy
slug: deploy
name: /harness:deploy
description: '- What was done'
prompt_preview: '---

  name: harness:deploy

  description: "Use when the user is done evolving and wants to finalize, clean up,
  tag the result, or push the optimized agent."

  allowed-tools: [Read, Write, Bash, Glob, AskUserQuestion]

  ---


  # /harness:deploy


  Finalize the evolution results. In v3, the best code is already in the main branch
  (auto-merged during evolve). Deploy is about cleanup, tagging, and pushing.


  ## What To Do


  ```bash

  TOOLS="${EVOLVER_TOOLS:-$([ -d ".evolver/tools" ] && echo ".evolver/tools" || echo...'
full_prompt_length: 2861
tools_mentioned:
- python
category: community
category_display: Community
source_repo: raphaelchristi/harness-evolver
source_path: skills/deploy/SKILL.md
source_url: https://github.com/raphaelchristi/harness-evolver/blob/main/skills/deploy/SKILL.md
fetched_at: '2026-07-05T06:06:25.999540+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-05T09:30:30.455844Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f63066e62a0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f63066e62a0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-05T09:51:18.549174Z'
indexed_at: '2026-07-05T09:51:18.549181Z'
---
