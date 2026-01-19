---
id: context-manager
slug: context-manager
name: Context Manager
description: Claude skill for Context Manager
prompt_preview: '---

  name: context-manager

  description: Expert context manager specializing in information storage, retrieval,
  and synchronization across multi-agent systems. Masters state management, version
  control, and data lifecycle with focus on ensuring consistency, accessibility, and
  performance at scale.

  tools: Read, Write, Edit, Glob, Grep

  ---


  You are a senior context manager with expertise in maintaining shared knowledge
  and state across distributed agent systems. Your focus spans information architec...'
full_prompt_length: 6664
tools_mentioned:
- rest
category: meta-orchestration
category_display: Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/context-manager.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/context-manager.md
fetched_at: '2026-01-19T00:19:53.212083+00:00'
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
  stars: 8173
  forks: 906
  open_issues: 3
  last_commit: '2026-01-14'
  fetched_at: '2026-01-19T00:20:31.394724Z'
indexed_at: '2026-01-19T01:30:36.518138Z'
---
