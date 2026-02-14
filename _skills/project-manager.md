---
id: project-manager
slug: project-manager
name: Project Manager
description: Claude skill for Project Manager
prompt_preview: '---

  name: project-manager

  description: "Use this agent when you need to establish project plans, track execution
  progress, manage risks, control budget/schedule, and coordinate stakeholders across
  complex initiatives."

  tools: Read, Write, Edit, Glob, Grep, WebFetch, WebSearch

  model: haiku

  ---


  You are a senior project manager with expertise in leading complex projects to successful
  completion. Your focus spans project planning, team coordination, risk management,
  and stakeholder communication wi...'
full_prompt_length: 6504
tools_mentioned: []
category: 08-business-product
category_display: 08 Business Product
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/08-business-product/project-manager.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/08-business-product/project-manager.md
fetched_at: '2026-02-14T04:10:01.803076Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:08:38.962329Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt is well-structured with clear sections and comprehensive
      checklists covering all major project management domains. However, it's incomplete
      (cuts off mid-sentence in Implementation Phase) and lacks specific instructions
      for tool usage or how to handle the incomplete context query protocol. The structured
      format with JSON examples is good, but the abrupt ending reduces clarity.
  usefulness:
    score: 4.5
    reasoning: The prompt provides extensive project management frameworks, methodologies,
      and practical checklists that would be highly valuable for real project management
      tasks. It covers planning, execution, risk management, and closure comprehensively.
      The main limitation is the incomplete implementation phase, which reduces immediate
      actionability.
  overall_rating: 4.25
  summary: A comprehensive project management prompt with excellent structure and
    practical frameworks, but incomplete execution instructions limit its immediate
    usability.
  tags_suggested:
  - project-management
  - business-planning
  - risk-management
  - agile-methodology
github_metrics:
  stars: 10374
  forks: 1101
  open_issues: 4
  last_commit: '2026-02-12'
  fetched_at: '2026-02-14T04:10:24.197233Z'
indexed_at: '2026-02-14T04:10:35.087251Z'
---
