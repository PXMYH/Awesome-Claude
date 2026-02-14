---
id: context-manager
slug: context-manager
name: Context Manager
description: Claude skill for Context Manager
prompt_preview: '---

  name: context-manager

  description: "Use for managing shared state, information retrieval, and data synchronization
  when multiple agents need coordinated access to context and metadata."

  tools: Read, Write, Edit, Glob, Grep

  model: sonnet

  ---


  You are a senior context manager with expertise in maintaining shared knowledge
  and state across distributed agent systems. Your focus spans information architecture,
  retrieval optimization, synchronization protocols, and data governance with emphasis
  on...'
full_prompt_length: 6571
tools_mentioned:
- rest
category: 09-meta-orchestration
category_display: 09 Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/context-manager.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/context-manager.md
fetched_at: '2026-02-14T04:10:04.267534Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:10:07.138978Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is highly specific and structured with clear categories
      and checklists, demonstrating strong prompt engineering practices. However,
      it's incomplete (ends abruptly at 'Document desi') and contains some vague instructions
      like 'Query system for context requirements' without specifying how. The communication
      protocol is defined but not fully integrated into actionable steps.
  usefulness:
    score: 4.0
    reasoning: The skill addresses a critical need in multi-agent systems—context
      management—with comprehensive coverage of storage, retrieval, synchronization,
      and lifecycle management. The detailed checklists and architecture patterns
      provide practical guidance for real-world implementation. The focus on performance
      metrics and compliance makes it highly actionable for developers building scalable
      agent systems.
  overall_rating: 3.75
  summary: A well-structured but incomplete prompt that provides valuable architectural
    guidance for context management in multi-agent systems, though execution clarity
    is hampered by abrupt termination and vague invocation instructions.
  tags_suggested:
  - multi-agent systems
  - context management
  - state synchronization
  - data architecture
  - performance optimization
github_metrics:
  stars: 10374
  forks: 1101
  open_issues: 4
  last_commit: '2026-02-12'
  fetched_at: '2026-02-14T04:10:24.197233Z'
indexed_at: '2026-02-14T04:10:35.117741Z'
---
