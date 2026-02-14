---
id: api-designer
slug: api-designer
name: Api Designer
description: Claude skill for Api Designer
prompt_preview: '---

  name: api-designer

  description: "Use this agent when designing new APIs, creating API specifications,
  or refactoring existing API architecture for scalability and developer experience.
  Invoke when you need REST/GraphQL endpoint design, OpenAPI documentation, authentication
  patterns, or API versioning strategies."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior API designer specializing in creating intuitive, scalable API architectures
  with expertise in REST and...'
full_prompt_length: 6115
tools_mentioned:
- GraphQL
- REST
category: core-development
category_display: Core Development
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/01-core-development/api-designer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/api-designer.md
fetched_at: '2026-02-14T04:09:30.739047Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:47:24.013085Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear role definition,
      comprehensive checklists, and detailed design principles. It follows excellent
      prompt engineering practices with organized sections and specific frameworks.
      However, it's slightly verbose and the progress reporting JSON is incomplete,
      which could cause confusion.
  usefulness:
    score: 5.0
    reasoning: This is highly practical for real-world API development, covering all
      critical aspects from REST/GraphQL design to authentication, documentation,
      and performance optimization. The systematic workflow and comprehensive checklists
      provide immediate value for developers designing production APIs. The inclusion
      of versioning strategies and backward compatibility considerations makes it
      enterprise-ready.
  overall_rating: 4.75
  summary: An outstanding API design prompt with exceptional comprehensiveness and
    practical value, though slightly verbose and containing one incomplete JSON example.
  tags_suggested:
  - api-design
  - rest-api
  - graphql
  - documentation
  - enterprise
github_metrics:
  stars: 10374
  forks: 1101
  open_issues: 4
  last_commit: '2026-02-12'
  fetched_at: '2026-02-14T04:10:24.197233Z'
indexed_at: '2026-02-14T04:10:34.681613Z'
---
