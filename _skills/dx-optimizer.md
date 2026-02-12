---
id: dx-optimizer
slug: dx-optimizer
name: Dx Optimizer
description: Claude skill for Dx Optimizer
prompt_preview: '---

  name: dx-optimizer

  description: "Use this agent when optimizing the complete developer workflow including
  build times, feedback loops, testing efficiency, and developer satisfaction metrics
  across the entire development environment."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---

  You are a senior DX optimizer with expertise in enhancing developer productivity
  and happiness. Your focus spans build optimization, development server performance,
  IDE configuration, and workflow auto...'
full_prompt_length: 6593
tools_mentioned: []
category: 06-developer-experience
category_display: 06 Developer Experience
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/06-developer-experience/dx-optimizer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/06-developer-experience/dx-optimizer.md
fetched_at: '2026-02-12T04:24:17.169439Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:03:30.659787Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt has strong structure with clear categories and a comprehensive
      checklist, but it's incomplete and contains a critical flaw. The 'Experience
      Analysis' section cuts off mid-sentence at 'Impl', leaving the workflow unfinished.
      While the DX optimization framework is well-organized, the abrupt termination
      undermines clarity and leaves key implementation steps undefined.
  usefulness:
    score: 4.0
    reasoning: The prompt outlines a valuable DX optimization framework covering build
      performance, tooling efficiency, and workflow automation with specific metrics
      and targets. However, its practical utility is limited by the incomplete workflow
      section, which prevents users from understanding the full implementation process.
      The comprehensive checklist and categories provide strong real-world value for
      developer productivity enhancement.
  overall_rating: 3.75
  summary: A well-structured but incomplete DX optimization prompt that provides a
    solid framework for developer experience enhancement but needs completion of the
    workflow section to be fully actionable.
  tags_suggested:
  - developer-experience
  - build-optimization
  - workflow-automation
  - performance-tuning
github_metrics:
  stars: 10218
  forks: 1093
  open_issues: 4
  last_commit: '2026-02-10'
  fetched_at: '2026-02-12T04:24:36.992823Z'
indexed_at: '2026-02-12T04:24:46.705544Z'
---
