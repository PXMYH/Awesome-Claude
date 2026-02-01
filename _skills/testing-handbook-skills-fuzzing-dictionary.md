---
id: testing-handbook-skills-fuzzing-dictionary
slug: testing-handbook-skills-fuzzing-dictionary
name: Fuzzing Dictionary
description: '**[OSS-Fuzz Dictionaries](https://github.com/google/oss-fuzz/tree/master/projects)**'
prompt_preview: "---\nname: fuzzing-dictionary\ntype: technique\ndescription: >\n\
  \  Fuzzing dictionaries guide fuzzers with domain-specific tokens.\n  Use when fuzzing\
  \ parsers, protocols, or format-specific code.\n---\n\n# Fuzzing Dictionary\n\n\
  A fuzzing dictionary provides domain-specific tokens to guide the fuzzer toward\
  \ interesting inputs. Instead of purely random mutations, the fuzzer incorporates\
  \ known keywords, magic numbers, protocol commands, and format-specific strings\
  \ that are more likely to reach deeper code pat..."
full_prompt_length: 9684
tools_mentioned:
- Rust
- go
- Go
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/testing-handbook-skills/skills/fuzzing-dictionary/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/testing-handbook-skills/skills/fuzzing-dictionary/SKILL.md
fetched_at: '2026-02-01T04:29:59.183731+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:26:33.163730Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured with comprehensive
      coverage of dictionary concepts, generation methods, and usage patterns. It
      follows best practices by providing concrete examples, command-line patterns,
      and step-by-step guidance. The only minor limitation is that the 'Common Patterns'
      section is cut off mid-example, which slightly reduces completeness.
  usefulness:
    score: 5.0
    reasoning: This skill provides immediate, practical value for security testing
      and fuzzing tasks. It covers real-world scenarios like protocol fuzzing and
      file format parsing with actionable commands and generation methods. The inclusion
      of cross-fuzzer compatibility (libFuzzer, AFL++, cargo-fuzz) makes it broadly
      applicable across different security testing workflows.
  overall_rating: 4.75
  summary: A highly effective security skill that provides comprehensive guidance
    on creating and using fuzzing dictionaries, with excellent practical examples
    and cross-tool compatibility.
  tags_suggested:
  - security
  - fuzzing
  - testing
  - protocol
  - parsing
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:51.020902Z'
indexed_at: '2026-02-01T04:32:51.020907Z'
---
