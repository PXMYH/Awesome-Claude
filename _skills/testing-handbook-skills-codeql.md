---
id: testing-handbook-skills-codeql
slug: testing-handbook-skills-codeql
name: CodeQL
description: '- [Blue-teaming for Exiv2: adding custom CodeQL queries to code scanning](https://github.blog/2021-11-16-adding-custom-codeql-queries-code-scanning/)'
prompt_preview: "---\nname: codeql\ntype: tool\ndescription: >\n  CodeQL is a static\
  \ analysis framework that queries code as a database.\n  Use when you need interprocedural\
  \ analysis or complex data flow tracking.\n---\n\n# CodeQL\n\nCodeQL is a powerful\
  \ static analysis framework that allows developers and security researchers to query\
  \ a codebase for specific code patterns. The CodeQL standard libraries implement\
  \ support for both inter- and intraprocedural control flow and data flow analysis.\
  \ However, the learning curve f..."
full_prompt_length: 19125
tools_mentioned:
- Python
- Go
- python
- go
- JavaScript
- java
- ruby
- TypeScript
- javascript
- Java
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/testing-handbook-skills/skills/codeql/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/testing-handbook-skills/skills/codeql/SKILL.md
fetched_at: '2026-01-19T00:20:21.619954+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:26:03.194499Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, a
      helpful quick reference table, and specific command examples. It follows best
      practices by defining when to use the tool versus alternatives, though it's
      cut off mid-sentence in the core workflow section, which slightly impacts completeness.
  usefulness:
    score: 4.0
    reasoning: This provides high real-world value for security professionals and
      developers needing deep code analysis, with actionable commands and installation
      instructions. However, the incomplete core workflow section and lack of query
      writing guidance limits its practical utility for users who need to create custom
      queries.
  overall_rating: 4.25
  summary: A well-structured and practical skill prompt for CodeQL that excels at
    providing clear usage guidance and commands, though it's incomplete and would
    benefit from query writing examples and troubleshooting guidance.
  tags_suggested:
  - security
  - static-analysis
  - codeql
  - developer-tools
  - security-scanning
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:36.818583Z'
indexed_at: '2026-01-19T01:30:36.818588Z'
---
