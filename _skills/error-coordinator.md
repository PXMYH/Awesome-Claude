---
id: error-coordinator
slug: error-coordinator
name: Error Coordinator
description: Claude skill for Error Coordinator
prompt_preview: '---

  name: error-coordinator

  description: Expert error coordinator specializing in distributed error handling,
  failure recovery, and system resilience. Masters error correlation, cascade prevention,
  and automated recovery strategies across multi-agent systems with focus on minimizing
  impact and learning from failures.

  tools: Read, Write, Edit, Glob, Grep

  ---


  You are a senior error coordination specialist with expertise in distributed system
  resilience, failure recovery, and continuous learning....'
full_prompt_length: 6930
tools_mentioned: []
category: 09-meta-orchestration
category_display: 09 Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/error-coordinator.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/error-coordinator.md
fetched_at: '2026-01-30T04:09:01.083929Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:10:17.305442Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt demonstrates strong structural organization with clear sections
      and technical depth, but suffers from incomplete content and abrupt termination.
      While the error coordination framework is comprehensive and well-structured,
      the development workflow section cuts off mid-sentence, creating ambiguity about
      execution steps.
  usefulness:
    score: 4.0
    reasoning: The prompt provides valuable, actionable error coordination strategies
      with concrete metrics and systematic approaches for distributed systems. It
      covers critical aspects like circuit breakers, retry strategies, and post-mortem
      automation that are highly relevant for production systems, though the incomplete
      workflow limits immediate implementation.
  overall_rating: 3.75
  summary: A technically sophisticated error coordination framework with strong architectural
    concepts, but requires completion of the development workflow section to achieve
    full practicality.
  tags_suggested:
  - distributed systems
  - error handling
  - resilience engineering
  - system orchestration
  - failure recovery
github_metrics:
  stars: 9096
  forks: 986
  open_issues: 2
  last_commit: '2026-01-26'
  fetched_at: '2026-01-30T04:09:16.735625Z'
indexed_at: '2026-01-30T04:09:18.441480Z'
---
