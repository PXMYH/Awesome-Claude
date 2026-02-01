---
id: sharp-edges-sharp-edges
slug: sharp-edges-sharp-edges
name: Sharp Edges Analysis
description: '- [ ] Probed all zero/empty/null edge cases'
prompt_preview: "---\nname: sharp-edges\ndescription: \"Identifies error-prone APIs,\
  \ dangerous configurations, and footgun designs that enable security mistakes. Use\
  \ when reviewing API designs, configuration schemas, cryptographic library ergonomics,\
  \ or evaluating whether code follows 'secure by default' and 'pit of success' principles.\
  \ Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous\
  \ configuration.\"\nallowed-tools:\n  - Read\n  - Grep\n  - Glob\n---\n\n# Sharp\
  \ Edges Analysis\n\nEvaluates wheth..."
full_prompt_length: 11424
tools_mentioned:
- rust
- Python
- JavaScript
- go
- PHP
- java
- Java
- Ruby
- TypeScript
- Go
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/sharp-edges/skills/sharp-edges/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/sharp-edges/skills/sharp-edges/SKILL.md
fetched_at: '2026-02-01T04:29:56.270904+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:23:57.675667Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, specific
      detection patterns, and concrete examples. It follows excellent prompt engineering
      practices with defined triggers, allowed tools, and explicit rejection of common
      rationalizations. The only minor weakness is the truncated content in the 'Primitive
      vs. Semantic APIs' section, which slightly impacts completeness.
  usefulness:
    score: 5.0
    reasoning: This prompt provides immediate, actionable value for security reviews
      with specific categories, detection patterns, and real-world examples like JWT
      and PHP password_hash. It directly addresses common security anti-patterns and
      gives evaluators a clear framework to identify dangerous API designs. The 'Rationalizations
      to Reject' table is particularly valuable for countering common developer pushback
      during security reviews.
  overall_rating: 4.75
  summary: An outstanding security analysis prompt that provides a comprehensive,
    actionable framework for identifying dangerous API designs and security footguns,
    with excellent structure and practical examples.
  tags_suggested:
  - security
  - api-design
  - cryptography
  - secure-by-default
  - footgun-analysis
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:50.980949Z'
indexed_at: '2026-02-01T04:32:50.980954Z'
---
