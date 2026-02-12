---
id: graphql-architect
slug: graphql-architect
name: Graphql Architect
description: Claude skill for Graphql Architect
prompt_preview: '---

  name: graphql-architect

  description: "Use this agent when designing or evolving GraphQL schemas across microservices,
  implementing federation architectures, or optimizing query performance in distributed
  graphs."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: opus

  ---


  You are a senior GraphQL architect specializing in schema design and distributed
  graph architectures with deep expertise in Apollo Federation 2.5+, GraphQL subscriptions,
  and performance optimization. Your primary focus is...'
full_prompt_length: 6550
tools_mentioned:
- WebSocket
- REST
- graphql
- GraphQL
category: core-development
category_display: Core Development
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/01-core-development/graphql-architect.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/graphql-architect.md
fetched_at: '2026-02-12T04:24:02.734069Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:48:38.749765Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt demonstrates strong technical specificity with comprehensive
      checklists covering GraphQL best practices, federation, and optimization strategies.
      However, it's incomplete (cut off mid-sentence in the implementation section)
      and lacks clear action instructions for the agent to execute, making it more
      of a reference guide than an operational prompt.
  usefulness:
    score: 4.5
    reasoning: The prompt provides exceptional real-world value for GraphQL architecture
      with detailed coverage of federation, subscriptions, and performance optimization.
      It's highly actionable for developers designing distributed GraphQL systems,
      though the incomplete structure limits immediate execution without additional
      context or completion.
  overall_rating: 4.25
  summary: A technically excellent but incomplete GraphQL architecture prompt that
    provides comprehensive best practices and checklists, though it needs completion
    and clearer execution instructions to be fully operational.
  tags_suggested:
  - GraphQL
  - API Design
  - Federation
  - Schema Architecture
  - Performance Optimization
github_metrics:
  stars: 10218
  forks: 1093
  open_issues: 4
  last_commit: '2026-02-10'
  fetched_at: '2026-02-12T04:24:36.992823Z'
indexed_at: '2026-02-12T04:24:46.417200Z'
---
