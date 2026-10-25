---
id: testing-handbook-skills-address-sanitizer
slug: testing-handbook-skills-address-sanitizer
name: AddressSanitizer (ASan)
description: 'Original research paper with technical details:'
prompt_preview: '---

  name: address-sanitizer

  type: technique

  description: "Builds and runs code under AddressSanitizer to catch buffer overflows,
  use-after-free, and other memory errors during fuzzing or tests. Covers -fsanitize=address
  builds, ASAN_OPTIONS, reading the crash report, LeakSanitizer, and the overhead
  and platform trade-offs. Use when fuzzing C/C++ or Rust that has unsafe blocks or
  FFI, when debugging a memory corruption crash, or when reading an ASan stack trace."

  ---


  # AddressSanitizer (ASan)


  A...'
full_prompt_length: 11543
tools_mentioned:
- rust
- go
- Java
- Go
- Rust
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/testing-handbook-skills/skills/address-sanitizer/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/testing-handbook-skills/skills/address-sanitizer/SKILL.md
fetched_at: '2026-10-25T07:20:41.851429+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:46:11.268491Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8debb530 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8debb530 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:09.020348Z'
indexed_at: '2026-10-25T12:12:09.020352Z'
---
