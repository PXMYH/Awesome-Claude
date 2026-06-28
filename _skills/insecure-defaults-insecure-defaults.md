---
id: insecure-defaults-insecure-defaults
slug: insecure-defaults-insecure-defaults
name: Insecure Defaults Detection
description: For detailed examples and counter-examples, see [examples.md](references/examples.md).
prompt_preview: '---

  name: insecure-defaults

  description: "Detects fail-open insecure defaults (hardcoded secrets, weak auth,
  permissive security) that allow apps to run insecurely in production. Use when auditing
  security, reviewing config management, or analyzing environment variable handling."

  allowed-tools: Read Grep Glob Bash

  ---


  # Insecure Defaults Detection


  Finds **fail-open** vulnerabilities where apps run insecurely with missing configuration.
  Distinguishes exploitable defaults from fail-secure patter...'
full_prompt_length: 5193
tools_mentioned:
- Docker
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/insecure-defaults/skills/insecure-defaults/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md
fetched_at: '2026-06-28T06:19:44.805005+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-28T09:55:11.850790Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a262f320 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a262f320 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-28T10:04:29.812443Z'
indexed_at: '2026-06-28T10:04:29.812449Z'
---
