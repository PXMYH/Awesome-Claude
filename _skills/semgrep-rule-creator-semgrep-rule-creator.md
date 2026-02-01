---
id: semgrep-rule-creator-semgrep-rule-creator
slug: semgrep-rule-creator-semgrep-rule-creator
name: Semgrep Rule Creator
description: 1. [Rule Syntax](https://semgrep.dev/docs/writing-rules/rule-syntax)
prompt_preview: "---\nname: semgrep-rule-creator\ndescription: Creates custom Semgrep\
  \ rules for detecting security vulnerabilities, bug patterns, and code patterns.\
  \ Use when writing Semgrep rules or building custom static analysis detections.\n\
  allowed-tools:\n  - Bash\n  - Read\n  - Write\n  - Edit\n  - Glob\n  - Grep\n  -\
  \ WebFetch\n---\n\n# Semgrep Rule Creator\n\nCreate production-quality Semgrep rules\
  \ with proper testing and validation.\n\n## When to Use\n\n**Ideal scenarios:**\n\
  - Writing Semgrep rules for specific bug patterns..."
full_prompt_length: 6679
tools_mentioned:
- python
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md
fetched_at: '2026-02-01T04:29:55.305689+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:23:47.720860Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt demonstrates strong clarity and specificity with clear usage
      guidelines, anti-patterns, and a strict workflow. It effectively defines scope
      through 'When to Use' and 'When NOT to Use' sections, and handles edge cases
      by rejecting common rationalizations. The only minor weakness is the incomplete
      sentence at the end, but the overall structure follows excellent prompt engineering
      practices.
  usefulness:
    score: 4.0
    reasoning: This skill provides high real-world value for security teams needing
      custom detection rules, covering both bug patterns and vulnerabilities. It's
      comprehensive with taint mode prioritization and testing requirements, though
      the strictness may limit casual users. The actionable workflow enables immediate
      benefit for developers familiar with Semgrep, but requires some learning curve
      for beginners.
  overall_rating: 4.25
  summary: A well-structured, production-focused skill that enforces rigorous testing
    and validation for Semgrep rule creation, ideal for security engineering teams
    but potentially too strict for casual use.
  tags_suggested:
  - security
  - static-analysis
  - semgrep
  - code-quality
  - vulnerability-detection
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:50.974187Z'
indexed_at: '2026-02-01T04:32:50.974193Z'
---
