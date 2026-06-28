---
id: certify
slug: certify
name: /harness:certify
description: 'If STABLE: suggest `/harness:deploy` to finalize.'
prompt_preview: '---

  name: harness:certify

  description: "Use when the user wants to verify that the evolved agent''s score
  is stable and reliable. Runs evaluation multiple times and reports mean ± std."

  allowed-tools: [Read, Bash, Glob]

  ---


  # /harness:certify


  Verify score stability by running evaluation multiple times and reporting statistical
  confidence.


  ## Resolve Tool Path


  ```bash

  TOOLS="${EVOLVER_TOOLS:-$([ -d ".evolver/tools" ] && echo ".evolver/tools" || echo
  "$HOME/.evolver/tools")}"

  EVOLVER_PY="${EVOL...'
full_prompt_length: 1999
tools_mentioned:
- python
category: community
category_display: Community
source_repo: raphaelchristi/harness-evolver
source_path: skills/certify/SKILL.md
source_url: https://github.com/raphaelchristi/harness-evolver/blob/main/skills/certify/SKILL.md
fetched_at: '2026-06-28T06:19:24.470049+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-28T09:42:46.214953Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a27d7d40 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a27d7d40 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-28T10:04:29.562505Z'
indexed_at: '2026-06-28T10:04:29.562510Z'
---
