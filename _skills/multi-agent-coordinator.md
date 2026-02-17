---
id: multi-agent-coordinator
slug: multi-agent-coordinator
name: Multi Agent Coordinator
description: Claude skill for Multi Agent Coordinator
prompt_preview: '---

  name: multi-agent-coordinator

  description: "Use when coordinating multiple concurrent agents that need to communicate,
  share state, synchronize work, and handle distributed failures across a system."

  tools: Read, Write, Edit, Glob, Grep

  model: opus

  ---


  You are a senior multi-agent coordinator with expertise in orchestrating complex
  distributed workflows. Your focus spans inter-agent communication, task dependency
  management, parallel execution control, and fault tolerance with emphasis on e...'
full_prompt_length: 6793
tools_mentioned:
- WebSocket
- GraphQL
- REST
category: 09-meta-orchestration
category_display: 09 Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/multi-agent-coordinator.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/multi-agent-coordinator.md
fetched_at: '2026-02-17T04:20:09.472153Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:10:49.698381Z'
  prompt_quality:
    score: 2.0
    reasoning: The prompt is highly ambiguous and incomplete, with the workflow analysis
      section abruptly cutting off mid-sentence ('Analyze'). While it attempts to
      be comprehensive with extensive checklists and categories, the instructions
      lack concrete action steps and clear execution guidance. The coordination context
      query is defined but not integrated into a coherent workflow, making it unclear
      how the agent should actually proceed.
  usefulness:
    score: 1.5
    reasoning: The prompt has limited practical value due to its incomplete nature
      and lack of actionable implementation details. While the concepts covered (coordination
      patterns, fault tolerance, etc.) are theoretically valuable for multi-agent
      systems, the prompt doesn't provide usable guidance for actual development tasks.
      The abrupt ending and vague instructions make it difficult for users to benefit
      immediately.
  overall_rating: 1.75
  summary: This prompt appears to be a work-in-progress draft that lists important
    multi-agent coordination concepts but fails to provide a complete, actionable
    framework for execution.
  tags_suggested:
  - meta-orchestration
  - multi-agent-systems
  - workflow-orchestration
  - distributed-systems
github_metrics:
  stars: 10561
  forks: 1120
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-17T04:20:20.236835Z'
indexed_at: '2026-02-17T04:20:38.092414Z'
---
