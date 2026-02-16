---
id: workflow-orchestrator
slug: workflow-orchestrator
name: Workflow Orchestrator
description: Claude skill for Workflow Orchestrator
prompt_preview: '---

  name: workflow-orchestrator

  description: "Use this agent when you need to design, implement, or optimize complex
  business process workflows with multiple states, error handling, and transaction
  management."

  tools: Read, Write, Edit, Glob, Grep

  model: opus

  ---


  You are a senior workflow orchestrator with expertise in designing and executing
  complex business processes. Your focus spans workflow modeling, state management,
  process orchestration, and error handling with emphasis on creating reli...'
full_prompt_length: 6580
tools_mentioned: []
category: 09-meta-orchestration
category_display: 09 Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/workflow-orchestrator.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/workflow-orchestrator.md
fetched_at: '2026-02-16T04:25:26.346696Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:11:28.656028Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is highly structured and specific about workflow orchestration
      concepts, with clear categories and checklists. However, it's incomplete (cuts
      off mid-sentence in Implementation Phase) and contains some vague instructions
      like 'Query context manager' without defining how to do so. The communication
      protocol is defined but not fully integrated into the workflow.
  usefulness:
    score: 4.0
    reasoning: The prompt provides comprehensive coverage of workflow orchestration
      patterns, error handling, and state management, making it valuable for complex
      process design. It includes practical checklists and categories that would guide
      real development tasks. The main limitation is the incomplete implementation
      section which reduces immediate actionability.
  overall_rating: 3.75
  summary: A well-structured but incomplete prompt that excels in covering workflow
    orchestration concepts comprehensively, though the truncated implementation phase
    limits its practical utility.
  tags_suggested:
  - workflow-orchestration
  - process-design
  - state-management
  - error-handling
  - business-process-automation
github_metrics:
  stars: 10503
  forks: 1111
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-16T04:25:43.240264Z'
indexed_at: '2026-02-16T04:26:01.914428Z'
---
