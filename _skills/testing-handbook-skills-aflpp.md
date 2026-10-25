---
id: testing-handbook-skills-aflpp
slug: testing-handbook-skills-aflpp
name: AFL++
description: '- [Fuzzing cURL](https://blog.trailofbits.com/2023/02/14/curl-audit-fuzzing-libcurl-command-line-interface/)
  - Trail of Bits blog post on using AFL++ argument fuzzing for cURL'
prompt_preview: '---

  name: aflpp

  type: fuzzer

  description: "Sets up and runs AFL++ for multi-core fuzzing of C/C++ projects built
  with afl-clang-fast or afl-gcc-fast. Covers instrumentation modes, parallel main
  and secondary campaigns, persistent mode, corpus minimization, and crash triage.
  Use when scaling fuzzing across cores, fuzzing a mature C/C++ codebase, reading
  the afl-fuzz status screen, or moving on after libFuzzer has plateaued."

  ---


  # AFL++


  AFL++ is a fork of the original AFL fuzzer that offers bet...'
full_prompt_length: 22378
tools_mentioned:
- docker
- Python
- Docker
- rest
- Rust
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/testing-handbook-skills/skills/aflpp/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/testing-handbook-skills/skills/aflpp/SKILL.md
fetched_at: '2026-10-25T07:20:41.963834+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:46:19.377202Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e5b5d60 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e5b5d60 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:09.022888Z'
indexed_at: '2026-10-25T12:12:09.022893Z'
---
