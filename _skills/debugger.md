---
id: debugger
slug: debugger
name: Debugger
description: Claude skill for Debugger
prompt_preview: '---

  name: debugger

  description: "Use this agent when you need to diagnose and fix bugs, identify root
  causes of failures, or analyze error logs and stack traces to resolve issues."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior debugging specialist with expertise in diagnosing complex software
  issues, analyzing system behavior, and identifying root causes. Your focus spans
  debugging techniques, tool mastery, and systematic problem-solving with emphasis
  on efficien...'
full_prompt_length: 6577
tools_mentioned: []
category: quality-security
category_display: Quality & Security
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/04-quality-security/debugger.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/debugger.md
fetched_at: '2026-02-11T04:28:55.698296Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:58:18.892298Z'
  prompt_quality:
    score: 3.0
    reasoning: The prompt demonstrates strong structure with clear categories and
      comprehensive technical coverage, but suffers from significant incompleteness.
      The 'Development Workflow' section cuts off mid-sentence at '2. Implemen', leaving
      critical instructions unfinished. While the debugging checklist and techniques
      are well-organized, the abrupt termination undermines clarity and prevents users
      from understanding the full workflow.
  usefulness:
    score: 4.0
    reasoning: Despite the incomplete structure, the prompt provides substantial practical
      value with extensive debugging methodologies, checklists, and technique categories
      that cover real-world scenarios. The systematic approach to root cause analysis
      and comprehensive coverage of debugging domains (memory, concurrency, performance,
      production) makes it highly actionable for developers. However, the missing
      workflow completion reduces its immediate usability.
  overall_rating: 3.5
  summary: A technically comprehensive debugging prompt with excellent coverage of
    debugging domains and methodologies, but critically undermined by an incomplete
    workflow section that cuts off mid-sentence, requiring completion before practical
    deployment.
  tags_suggested:
  - debugging
  - quality-assurance
  - systematic-analysis
  - root-cause-analysis
  - technical-troubleshooting
github_metrics:
  stars: 10153
  forks: 1087
  open_issues: 3
  last_commit: '2026-02-10'
  fetched_at: '2026-02-11T04:29:28.992841Z'
indexed_at: '2026-02-11T04:29:38.993177Z'
---
