---
id: c-review-c-review
slug: c-review-c-review
name: C/C++ Security Review
description: '- Every Phase-5 cluster task is `completed` (verify via `TaskList`).'
prompt_preview: '---

  name: c-review

  description: Performs comprehensive C/C++ security review for memory corruption,
  integer overflows, race conditions, and platform-specific vulnerabilities. Use when
  auditing native C/C++ applications, reviewing daemons or services for memory safety,
  or hunting integer overflow / use-after-free / race conditions in userspace code.

  allowed-tools: Agent AskUserQuestion SendMessage TaskCreate TaskUpdate TaskList
  TaskGet Grep Glob Read Write Bash

  ---


  # C/C++ Security Review


  Runs...'
full_prompt_length: 24410
tools_mentioned:
- Rust
- Java
- Python
- Go
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/c-review/skills/c-review/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/c-review/skills/c-review/SKILL.md
fetched_at: '2026-06-07T06:28:56.551135+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-07T09:54:10.826905Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffc32bd0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f44ffc32bd0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-07T10:04:55.681297Z'
indexed_at: '2026-06-07T10:04:55.681320Z'
---
