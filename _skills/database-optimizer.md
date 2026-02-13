---
id: database-optimizer
slug: database-optimizer
name: Database Optimizer
description: Claude skill for Database Optimizer
prompt_preview: '---

  name: database-optimizer

  description: "Use this agent when you need to analyze slow queries, optimize database
  performance across multiple systems, or implement indexing strategies to improve
  query execution."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior database optimizer with expertise in performance tuning across
  multiple database systems. Your focus spans query optimization, index design, execution
  plan analysis, and system configuration with emphasis on...'
full_prompt_length: 6553
tools_mentioned:
- Redis
- MongoDB
- PostgreSQL
- MySQL
category: 05-data-ai
category_display: 05 Data Ai
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/05-data-ai/database-optimizer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/05-data-ai/database-optimizer.md
fetched_at: '2026-02-13T04:21:02.961241Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:00:47.164268Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is highly specific and structured, providing a clear checklist
      and detailed categories for database optimization. However, it is incomplete,
      cutting off mid-sentence in the 'Implementation Phase' section, which introduces
      ambiguity and lacks a defined conclusion or final instructions.
  usefulness:
    score: 4.0
    reasoning: The skill offers comprehensive coverage of database optimization topics,
      including specific metrics and strategies for multiple database systems, making
      it highly practical for real-world performance tuning tasks. The structured
      checklist and categories provide actionable guidance for users.
  overall_rating: 3.75
  summary: A detailed and practical database optimization skill that is let down by
    an incomplete prompt structure, though its content remains valuable for performance
    tuning tasks.
  tags_suggested:
  - database optimization
  - performance tuning
  - query analysis
github_metrics:
  stars: 10303
  forks: 1096
  open_issues: 3
  last_commit: '2026-02-12'
  fetched_at: '2026-02-13T04:21:22.535205Z'
indexed_at: '2026-02-13T04:21:32.008712Z'
---
