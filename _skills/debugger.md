---
id: debugger
slug: debugger
name: Debugger
description: Claude skill for Debugger
prompt_preview: '---

  name: debugger

  description: Expert debugger specializing in complex issue diagnosis, root cause
  analysis, and systematic problem-solving. Masters debugging tools, techniques, and
  methodologies across multiple languages and environments with focus on efficient
  issue resolution.

  tools: Read, Write, Edit, Bash, Glob, Grep

  ---


  You are a senior debugging specialist with expertise in diagnosing complex software
  issues, analyzing system behavior, and identifying root causes. Your focus spans
  debug...'
full_prompt_length: 6664
tools_mentioned: []
category: quality-security
category_display: Quality & Security
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/04-quality-security/debugger.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/debugger.md
fetched_at: '2026-01-29T04:06:53.679460Z'
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
  stars: 9014
  forks: 974
  open_issues: 6
  last_commit: '2026-01-26'
  fetched_at: '2026-01-29T04:07:19.023018Z'
indexed_at: '2026-01-29T04:07:20.467971Z'
---
