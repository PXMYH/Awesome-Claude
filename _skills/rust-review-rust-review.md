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
- rest
- Rust
- rust
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/rust-review/skills/rust-review/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/rust-review/skills/rust-review/SKILL.md
fetched_at: '2026-07-19T05:24:20.718568+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-07-19T09:04:36.829470Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101c0cb0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ff2101c0cb0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-07-19T09:13:21.734191Z'
indexed_at: '2026-07-19T09:13:21.734197Z'
---
