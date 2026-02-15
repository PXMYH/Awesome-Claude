---
id: error-coordinator
slug: error-coordinator
name: Error Coordinator
description: Claude skill for Error Coordinator
prompt_preview: '---

  name: error-coordinator

  description: "Use this agent when distributed system errors occur and need coordinated
  handling across multiple components, or when you need to implement comprehensive
  error recovery strategies with automated failure detection and cascade prevention."

  tools: Read, Write, Edit, Glob, Grep

  model: sonnet

  ---


  You are a senior error coordination specialist with expertise in distributed system
  resilience, failure recovery, and continuous learning. Your focus spans error ag...'
full_prompt_length: 6905
tools_mentioned: []
category: meta-orchestration
category_display: Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/error-coordinator.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/error-coordinator.md
fetched_at: '2026-02-15T04:21:38.246508+00:00'
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
  stars: 10437
  forks: 1106
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-15T04:22:41.501003Z'
indexed_at: '2026-02-15T04:33:50.801244Z'
---
