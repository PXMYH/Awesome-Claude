---
id: frontend-developer
slug: frontend-developer
name: Frontend Developer
description: Claude skill for Frontend Developer
prompt_preview: '---

  name: frontend-developer

  description: "Use when building complete frontend applications across React, Vue,
  and Angular frameworks requiring multi-framework expertise and full-stack integration.
  Specifically:\n\n<example>\nContext: Starting a new React frontend for an e-commerce
  platform with complex state management and real-time updates\nuser: \"Build a React
  frontend for product catalog with filtering, cart management, and checkout flow.
  Need TypeScript, responsive design, and 85% test cov...'
full_prompt_length: 7220
tools_mentioned:
- TypeScript
- PHP
- Vue
- websocket
- React
- Angular
- WebSocket
category: core-development
category_display: Core Development
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/01-core-development/frontend-developer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/frontend-developer.md
fetched_at: '2026-02-09T04:26:03.891354Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:48:07.898876Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is highly structured and clear, providing a mandatory context-gathering
      step and a detailed execution flow. It specifies tools, communication protocols,
      and deliverables, which reduces ambiguity. However, the prompt is incomplete
      (cut off mid-sentence in the deliverables section), which slightly impacts its
      completeness and could lead to confusion about final requirements.
  usefulness:
    score: 4.0
    reasoning: This prompt is practical for real-world frontend development, emphasizing
      maintainability, testing, and accessibility. It guides the agent through a logical
      workflow from context discovery to handoff, which is valuable for complex projects.
      However, the incomplete deliverables list and some overly specific requirements
      (like exact TypeScript config) may limit its broad applicability without customization.
  overall_rating: 4.25
  summary: A well-structured and actionable prompt for frontend development tasks,
    though its incomplete state reduces its immediate usability and requires completion
    for full effectiveness.
  tags_suggested:
  - frontend
  - react
  - typescript
  - development workflow
  - accessibility
github_metrics:
  stars: 9985
  forks: 1081
  open_issues: 3
  last_commit: '2026-02-07'
  fetched_at: '2026-02-09T04:26:32.597214Z'
indexed_at: '2026-02-09T04:26:41.851084Z'
---
