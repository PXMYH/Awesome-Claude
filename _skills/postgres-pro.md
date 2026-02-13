---
id: postgres-pro
slug: postgres-pro
name: Postgres Pro
description: Claude skill for Postgres Pro
prompt_preview: '---

  name: postgres-pro

  description: "Use when you need to optimize PostgreSQL performance, design high-availability
  replication, or troubleshoot database issues at scale. Invoke this agent for query
  optimization, configuration tuning, replication setup, backup strategies, and mastering
  advanced PostgreSQL features for enterprise deployments."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior PostgreSQL expert with mastery of database administration and optimization....'
full_prompt_length: 6537
tools_mentioned:
- PostgreSQL
category: 05-data-ai
category_display: 05 Data Ai
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/05-data-ai/postgres-pro.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/05-data-ai/postgres-pro.md
fetched_at: '2026-02-13T04:21:03.926446Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:02:11.704454Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is well-structured with clear sections and specific technical
      domains, but it is incomplete and lacks a defined completion mechanism. The
      workflow section cuts off mid-sentence, and there is no explicit instruction
      on how the agent should conclude its analysis or present findings to the user.
  usefulness:
    score: 4.0
    reasoning: The prompt provides a comprehensive framework for PostgreSQL optimization,
      covering critical areas like performance tuning, replication, and high availability.
      The inclusion of specific metrics and architecture details makes it highly actionable
      for database administrators.
  overall_rating: 3.75
  summary: A technically robust prompt that is strong in scope and detail but suffers
    from structural incompleteness, limiting its immediate operational utility.
  tags_suggested:
  - PostgreSQL
  - Database Administration
  - Performance Tuning
  - High Availability
  - DevOps
github_metrics:
  stars: 10303
  forks: 1096
  open_issues: 3
  last_commit: '2026-02-12'
  fetched_at: '2026-02-13T04:21:22.535205Z'
indexed_at: '2026-02-13T04:21:32.030977Z'
---
