---
id: semgrep-rule-creator-semgrep-rule-creator
slug: semgrep-rule-creator-semgrep-rule-creator
name: Semgrep Rule Creator
description: '- For detailed workflow and examples, see [workflow.md]({baseDir}/references/workflow.md)'
prompt_preview: "---\nname: semgrep-rule-creator\ndescription: Create custom Semgrep\
  \ rules for detecting bug patterns and security vulnerabilities. This skill should\
  \ be used when the user explicitly asks to \"create a Semgrep rule\", \"write a\
  \ Semgrep rule\", \"make a Semgrep rule\", \"build a Semgrep rule\", or requests\
  \ detection of a specific bug pattern, vulnerability, or insecure code pattern using\
  \ Semgrep.\nallowed-tools:\n  - Bash\n  - Read\n  - Write\n  - Edit\n  - Glob\n\
  \  - Grep\n  - WebFetch\n---\n\n# Semgrep Rule Creator..."
full_prompt_length: 8462
tools_mentioned:
- python
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md
fetched_at: '2026-01-25T03:52:40.835666+00:00'
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
  fetched_at: '2026-01-25T04:05:53.112238Z'
indexed_at: '2026-01-25T04:05:53.112244Z'
---
