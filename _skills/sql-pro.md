---
id: sql-pro
slug: sql-pro
name: Sql Pro
description: Claude skill for Sql Pro
prompt_preview: '---

  name: sql-pro

  description: Expert SQL developer specializing in complex query optimization, database
  design, and performance tuning across PostgreSQL, MySQL, SQL Server, and Oracle.
  Masters advanced SQL features, indexing strategies, and data warehousing patterns.

  tools: Read, Write, Edit, Bash, Glob, Grep

  ---


  You are a senior SQL developer with mastery across major database systems (PostgreSQL,
  MySQL, SQL Server, Oracle), specializing in complex query design, performance optimization,
  and...'
full_prompt_length: 7373
tools_mentioned:
- rest
- python
- MySQL
- java
- PostgreSQL
category: language-specialists
category_display: Language Specialists
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/02-language-specialists/sql-pro.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/02-language-specialists/sql-pro.md
fetched_at: '2026-01-26T03:55:58.515723Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:53:35.767170Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt is highly specific and well-structured, clearly defining
      the agent's expertise across multiple database systems and advanced SQL features.
      It follows good prompt engineering practices with structured sections and checklists.
      However, it's incomplete - the development workflow section is cut off mid-sentence,
      and the communication protocol lacks implementation details for how the agent
      should actually request context from users.
  usefulness:
    score: 4.5
    reasoning: This is an extremely practical and comprehensive SQL development skill
      that covers real-world scenarios like query optimization, performance tuning,
      and database architecture. The extensive checklists and pattern references provide
      immediate value for developers working with complex databases. The inclusion
      of specific database features and security considerations makes it highly actionable
      for enterprise development tasks.
  overall_rating: 4.25
  summary: A well-conceived SQL development skill with comprehensive coverage of database
    expertise and optimization techniques, though the prompt is incomplete and would
    benefit from a complete development workflow and clearer user interaction protocols.
  tags_suggested:
  - SQL
  - Database
  - Performance
  - Optimization
  - PostgreSQL
  - MySQL
  - SQL Server
  - Oracle
github_metrics:
  stars: 8759
  forks: 958
  open_issues: 5
  last_commit: '2026-01-14'
  fetched_at: '2026-01-26T03:56:25.412385Z'
indexed_at: '2026-01-26T03:56:26.484565Z'
---
