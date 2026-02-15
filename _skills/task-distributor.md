---
id: task-distributor
slug: task-distributor
name: Task Distributor
description: Claude skill for Task Distributor
prompt_preview: '---

  name: task-distributor

  description: "Use when distributing tasks across multiple agents or workers, managing
  queues, and balancing workloads to maximize throughput while respecting priorities
  and deadlines."

  tools: Read, Write, Edit, Glob, Grep

  model: haiku

  ---


  You are a senior task distributor with expertise in optimizing work allocation across
  distributed systems. Your focus spans queue management, load balancing algorithms,
  priority scheduling, and resource optimization with emphasis on...'
full_prompt_length: 6668
tools_mentioned: []
category: meta-orchestration
category_display: Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/task-distributor.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/task-distributor.md
fetched_at: '2026-02-15T04:21:39.006005+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:11:18.746648Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt demonstrates strong conceptual structure with clear categories
      and checklists, but suffers from significant incompleteness. The Development
      Workflow section is truncated mid-sentence ('Pla' instead of 'Plan'), and the
      prompt lacks concrete implementation details or examples. While the framework
      is comprehensive, the abrupt ending and missing content reduce clarity and practical
      utility.
  usefulness:
    score: 3.0
    reasoning: The prompt outlines valuable orchestration concepts relevant to distributed
      systems, but its incomplete nature limits immediate practical application. The
      extensive checklists and categories provide a solid theoretical foundation,
      but without executable guidance or examples, users would struggle to implement
      the described strategies effectively.
  overall_rating: 3.25
  summary: A well-structured but incomplete prompt that establishes a comprehensive
    framework for task distribution orchestration, though its truncated development
    workflow and lack of concrete implementation details prevent it from being fully
    actionable.
  tags_suggested:
  - meta-orchestration
  - task-distribution
  - load-balancing
  - queue-management
  - distributed-systems
github_metrics:
  stars: 10437
  forks: 1106
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-15T04:22:41.501003Z'
indexed_at: '2026-02-15T04:33:50.820305Z'
---
