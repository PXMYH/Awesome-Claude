---
id: fp-check-fp-check
slug: fp-check-fp-check
name: False Positive Check
description: '- [Standard Verification]({baseDir}/references/standard-verification.md)
  — Linear single-pass checklist for straightforward bugs'
prompt_preview: '---

  name: fp-check

  description: "Systematically verifies suspected security bugs to eliminate false
  positives, producing a TRUE POSITIVE or FALSE POSITIVE verdict with documented evidence
  for each. Use when asked whether a specific finding is real, exploitable, or a false
  positive, or to verify or validate a suspected vulnerability — not for hunting or
  discovering new bugs."

  allowed-tools: Read Grep Glob LSP Bash Task Write Edit AskUserQuestion TaskCreate
  TaskUpdate TaskList TaskGet

  ---


  # False...'
full_prompt_length: 6723
tools_mentioned: []
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/fp-check/skills/fp-check/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/fp-check/skills/fp-check/SKILL.md
fetched_at: '2026-07-19T05:24:18.745614+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T09:03:31.699520Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101c3440 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101c3440 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:21.709363Z'
indexed_at: '2026-07-19T09:13:21.709369Z'
---
