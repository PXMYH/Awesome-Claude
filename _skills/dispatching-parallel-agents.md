---
id: dispatching-parallel-agents
slug: dispatching-parallel-agents
name: Dispatching Parallel Agents
description: 'From debugging session (2025-10-03):'
prompt_preview: '---

  name: dispatching-parallel-agents

  description: Use when facing 2+ independent tasks that can be worked on without
  shared state or sequential dependencies

  ---


  # Dispatching Parallel Agents


  ## Overview


  When you have multiple unrelated failures (different test files, different subsystems,
  different bugs), investigating them sequentially wastes time. Each investigation
  is independent and can happen in parallel.


  **Core principle:** Dispatch one agent per independent problem domain. Let them
  w...'
full_prompt_length: 6082
tools_mentioned:
- typescript
category: community
category_display: Community Skills
source_repo: obra/superpowers
source_path: skills/dispatching-parallel-agents/SKILL.md
source_url: https://github.com/obra/superpowers/blob/main/skills/dispatching-parallel-agents/SKILL.md
fetched_at: '2026-02-05T04:14:31.503491Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:17:20.997249Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, visual
      flowcharts, and concrete examples. It follows best practices by providing specific
      constraints, output formats, and common mistakes. The only minor weakness is
      the incomplete 'Vague output:' section in Common Mistakes, which slightly reduces
      completeness.
  usefulness:
    score: 5.0
    reasoning: This is highly practical for real development workflows where multiple
      independent failures occur. The pattern directly addresses a common pain point
      in debugging and testing, providing immediately actionable guidance. The examples
      and agent prompt structure are directly transferable to actual use cases.
  overall_rating: 4.75
  summary: An excellent, production-ready prompt that effectively teaches a valuable
    parallelization pattern with clear structure, practical examples, and actionable
    guidance.
  tags_suggested:
  - parallelization
  - debugging
  - testing
  - agent orchestration
  - workflow optimization
github_metrics:
  stars: 44605
  forks: 3386
  open_issues: 131
  last_commit: '2026-01-30'
  fetched_at: '2026-02-05T04:14:40.551804Z'
indexed_at: '2026-02-05T04:14:41.402937Z'
---
