---
id: constant-time-analysis-constant-time-analysis
slug: constant-time-analysis-constant-time-analysis
name: Constant-Time Analysis
description: '- [Cryptocoding Guidelines](https://github.com/veorq/cryptocoding) -
  Defensive coding for crypto'
prompt_preview: '---

  name: constant-time-analysis

  description: Detects timing side-channel vulnerabilities in cryptographic code.
  Use when implementing or reviewing crypto code, encountering division on secrets,
  secret-dependent branches, or constant-time programming questions in C, C++, Go,
  Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby.

  ---


  # Constant-Time Analysis


  Analyze cryptographic code to detect operations that leak secret data through execution
  timing variations.


  ## When...'
full_prompt_length: 9912
tools_mentioned:
- Python
- Node.js
- Go
- python
- go
- JavaScript
- php
- java
- ruby
- Rust
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md
fetched_at: '2026-01-19T00:20:15.331690+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:22:20.420326Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear triggers, language-specific
      guidance, and practical examples. The flowchart for 'When to Use' is innovative
      and effective. However, it references external files (references/*.md) that
      aren't provided, which could limit immediate usability without those resources.
  usefulness:
    score: 5.0
    reasoning: This addresses a critical security concern in cryptographic implementation
      with concrete, actionable guidance. The language-specific references and command
      examples make it immediately practical for developers working across multiple
      programming languages. The focus on real-world vulnerabilities like KyberSlash
      shows deep domain expertise.
  overall_rating: 4.75
  summary: An excellent, production-ready security skill prompt that provides comprehensive
    guidance for detecting timing side-channel vulnerabilities across multiple languages
    with practical implementation examples.
  tags_suggested:
  - security
  - cryptography
  - side-channel
  - timing-attacks
  - code-review
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:36.749907Z'
indexed_at: '2026-01-19T01:30:36.749915Z'
---
