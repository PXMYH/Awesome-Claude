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
category_display: Community
source_repo: obra/superpowers
source_path: skills/dispatching-parallel-agents/SKILL.md
source_url: https://github.com/obra/superpowers/blob/main/skills/dispatching-parallel-agents/SKILL.md
fetched_at: '2026-02-22T04:16:22.345923+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-02-22T05:04:33.445438Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fc93251d310 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fc93251d310 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 57121
  forks: 4328
  open_issues: 140
  last_commit: '2026-02-21'
  fetched_at: '2026-02-22T04:17:15.657532Z'
indexed_at: '2026-02-22T05:20:56.692397Z'
---
