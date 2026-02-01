---
id: testing-handbook-skills-address-sanitizer
slug: testing-handbook-skills-address-sanitizer
name: AddressSanitizer (ASan)
description: 'Original research paper with technical details:'
prompt_preview: "---\nname: address-sanitizer\ntype: technique\ndescription: >\n \
  \ AddressSanitizer detects memory errors during fuzzing.\n  Use when fuzzing C/C++\
  \ code to find buffer overflows and use-after-free bugs.\n---\n\n# AddressSanitizer\
  \ (ASan)\n\nAddressSanitizer (ASan) is a widely adopted memory error detection tool\
  \ used extensively during software testing, particularly fuzzing. It helps detect\
  \ memory corruption bugs that might otherwise go unnoticed, such as buffer overflows,\
  \ use-after-free errors, and other mem..."
full_prompt_length: 11272
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
fetched_at: '2026-02-01T04:29:57.945162+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:25:01.463899Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured, using markdown
      formatting, tables, and code blocks effectively. It provides specific commands
      and configuration options, though it slightly truncates the 'Understanding ASan
      Reports' section, which is a minor completeness issue.
  usefulness:
    score: 5.0
    reasoning: This is a highly practical and comprehensive guide for using AddressSanitizer
      in fuzzing scenarios. It covers essential steps from compilation to configuration,
      includes real-world patterns, and provides actionable commands that developers
      can immediately apply to find memory safety vulnerabilities in C/C++ code.
  overall_rating: 4.75
  summary: An excellent, production-ready prompt that effectively teaches AddressSanitizer
    usage for fuzzing with clear structure, practical examples, and comprehensive
    coverage of key concepts and commands.
  tags_suggested:
  - fuzzing
  - memory-safety
  - security-testing
  - C++
  - vulnerability-detection
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:50.997891Z'
indexed_at: '2026-02-01T04:32:50.997896Z'
---
