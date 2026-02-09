---
id: workflow-orchestrator
slug: workflow-orchestrator
name: Workflow Orchestrator
description: Claude skill for Workflow Orchestrator
prompt_preview: '---

  name: workflow-orchestrator

  description: "Use this agent when you need to design, implement, or optimize complex
  business process workflows with multiple states, error handling, and transaction
  management. Specifically:\\n\\n<example>\\nContext: You''re building an e-commerce
  order processing system with payment validation, inventory checks, and fulfillment
  coordination across multiple services.\\nuser: \"I need to design a workflow that
  handles order processing with rollback capabilities if...'
full_prompt_length: 8780
tools_mentioned: []
category: 09-meta-orchestration
category_display: 09 Meta Orchestration
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/09-meta-orchestration/workflow-orchestrator.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/09-meta-orchestration/workflow-orchestrator.md
fetched_at: '2026-02-09T04:26:22.833870Z'
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
  stars: 9985
  forks: 1081
  open_issues: 3
  last_commit: '2026-02-07'
  fetched_at: '2026-02-09T04:26:32.597214Z'
indexed_at: '2026-02-09T04:26:42.304347Z'
---
