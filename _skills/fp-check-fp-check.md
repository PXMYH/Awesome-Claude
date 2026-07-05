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
fetched_at: '2026-07-05T06:06:47.426067+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-05T09:41:26.846994Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f6306739f10 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f6306739f10 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-05T09:51:18.778187Z'
indexed_at: '2026-07-05T09:51:18.778193Z'
---
