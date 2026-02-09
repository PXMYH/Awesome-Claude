---
id: sql-pro
slug: sql-pro
name: Sql Pro
description: Claude skill for Sql Pro
prompt_preview: '---

  name: sql-pro

  description: "Use this agent when you need to optimize complex SQL queries, design
  efficient database schemas, or solve performance issues across PostgreSQL, MySQL,
  SQL Server, and Oracle requiring advanced query optimization, index strategies,
  or data warehouse patterns. Specifically:\\n\\n<example>\\nContext: User has a slow
  analytical query in PostgreSQL running against 100M+ row tables that joins 5 tables
  and uses window functions but takes 8+ seconds. Needs to meet <500ms...'
full_prompt_length: 10210
tools_mentioned:
- python
- PostgreSQL
- java
- rest
- MySQL
category: language-specialists
category_display: Language Specialists
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/02-language-specialists/sql-pro.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/02-language-specialists/sql-pro.md
fetched_at: '2026-02-09T04:26:08.337181Z'
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
  stars: 9985
  forks: 1081
  open_issues: 3
  last_commit: '2026-02-07'
  fetched_at: '2026-02-09T04:26:32.597214Z'
indexed_at: '2026-02-09T04:26:41.962300Z'
---
