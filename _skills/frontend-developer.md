---
id: frontend-developer
slug: frontend-developer
name: Frontend Developer
description: Claude skill for Frontend Developer
prompt_preview: '---

  name: frontend-developer

  description: Expert UI engineer focused on crafting robust, scalable frontend solutions.
  Builds high-quality React components prioritizing maintainability, user experience,
  and web standards compliance.

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior frontend developer specializing in modern web applications with
  deep expertise in React 18+, Vue 3+, and Angular 15+. Your primary focus is building
  performant, accessible, and maintainable...'
full_prompt_length: 4573
tools_mentioned:
- Angular
- WebSocket
- websocket
- TypeScript
- React
- Vue
category: core-development
category_display: Core Development
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/01-core-development/frontend-developer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/01-core-development/frontend-developer.md
fetched_at: '2026-01-31T04:04:27.599303Z'
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
  stars: 9155
  forks: 995
  open_issues: 1
  last_commit: '2026-01-30'
  fetched_at: '2026-01-31T04:05:02.395696Z'
indexed_at: '2026-01-31T04:05:03.531764Z'
---
