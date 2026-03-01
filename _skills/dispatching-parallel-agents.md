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
fetched_at: '2026-03-01T04:22:17.342534+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-03-01T05:19:18.049361Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f6f7bbaa900 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f6f7bbaa900 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 66086
  forks: 5046
  open_issues: 186
  last_commit: '2026-02-21'
  fetched_at: '2026-03-01T04:22:54.491304Z'
indexed_at: '2026-03-01T05:39:09.427064Z'
---
