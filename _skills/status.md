---
id: status
slug: status
name: /harness:status
description: '- Detect stagnation: if last 3 scores within 1% of each other, warn
  and suggest `/harness:evolve` with architect trigger.'
prompt_preview: '---

  name: harness:status

  description: "Use when the user asks about evolution progress, current scores, best
  version, how many iterations ran, or whether the loop is stagnating."

  allowed-tools: [Read, Bash]

  ---


  # /harness:status


  Show current evolution progress.


  ## What To Do


  ### Resolve Tool Path


  ```bash

  TOOLS="${EVOLVER_TOOLS:-$([ -d ".evolver/tools" ] && echo ".evolver/tools" || echo
  "$HOME/.evolver/tools")}"

  EVOLVER_PY="${EVOLVER_PY:-$([ -f "$HOME/.evolver/venv/bin/python" ] && echo "$HO...'
full_prompt_length: 969
tools_mentioned:
- python
category: community
category_display: Community
source_repo: raphaelchristi/harness-evolver
source_path: skills/status/SKILL.md
source_url: https://github.com/raphaelchristi/harness-evolver/blob/main/skills/status/SKILL.md
fetched_at: '2026-06-21T06:52:48.312637+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-21T10:13:59.730732Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9ac8fb0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fbaa9ac8fb0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-21T10:34:03.465300Z'
indexed_at: '2026-06-21T10:34:03.465306Z'
---
