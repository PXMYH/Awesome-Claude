---
id: rust-review-rust-review
slug: rust-review-rust-review
name: Rust Security Review
description: '- Every Phase-5 cluster task is `completed` (verify via `TaskList`).'
prompt_preview: '---

  name: rust-review

  description: Performs comprehensive Rust security review for safe/unsafe boundary
  issues, memory safety in unsafe blocks, concurrency hazards, panic-induced DoS,
  FFI safety, and async runtime mistakes. Use when auditing Rust crates, services,
  or libraries — particularly those with `unsafe`, FFI, or concurrent code.

  allowed-tools: Agent AskUserQuestion SendMessage TaskCreate TaskUpdate TaskList
  Read Write Bash

  ---


  # Rust Security Review


  Runs in the main conversation (invok...'
full_prompt_length: 43919
tools_mentioned:
- rust
- rest
- Rust
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/rust-review/skills/rust-review/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/rust-review/skills/rust-review/SKILL.md
fetched_at: '2026-07-05T06:06:49.599054+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-05T09:42:31.975878Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f6306575a90 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f6306575a90 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-05T09:51:18.801257Z'
indexed_at: '2026-07-05T09:51:18.801263Z'
---
