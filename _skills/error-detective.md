---
id: error-detective
slug: error-detective
name: Error Detective
description: Claude skill for Error Detective
prompt_preview: '---

  name: error-detective

  description: "Use this agent when you need to diagnose why errors are occurring
  in your system, correlate errors across services, identify root causes, and prevent
  future failures. Specifically:\\n\\n<example>\\nContext: Production system is experiencing
  intermittent failures across multiple microservices with unclear root cause.\\nuser:
  \"We have 50+ errors per minute in production with timeout exceptions in the API
  gateway, database connection errors, and queue failur...'
full_prompt_length: 9860
tools_mentioned: []
category: quality-security
category_display: Quality & Security
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/04-quality-security/error-detective.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/04-quality-security/error-detective.md
fetched_at: '2026-02-10T04:30:23.386014Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:58:40.891753Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt is highly structured with clear sections and comprehensive
      checklists covering error detection methodologies. However, it's incomplete
      - the Development Workflow section cuts off mid-sentence during 'Data collection',
      and the prompt lacks specific instructions for tool usage or how to structure
      actual responses. The communication protocol is defined but not fully integrated
      into actionable steps.
  usefulness:
    score: 4.5
    reasoning: This provides exceptional real-world value for debugging complex distributed
      systems with its systematic approach to error correlation and root cause analysis.
      The comprehensive checklists and methodologies (Five Whys, Fishbone diagrams,
      etc.) offer practical frameworks that developers can immediately apply. The
      focus on preventing error cascades and predictive monitoring addresses critical
      production needs.
  overall_rating: 4.25
  summary: A well-structured but incomplete prompt that excels in providing systematic
    error analysis frameworks but needs completion of the workflow section and clearer
    tool integration instructions.
  tags_suggested:
  - debugging
  - distributed-systems
  - error-analysis
  - root-cause-analysis
  - production-monitoring
github_metrics:
  stars: 10075
  forks: 1084
  open_issues: 3
  last_commit: '2026-02-07'
  fetched_at: '2026-02-10T04:30:47.641906Z'
indexed_at: '2026-02-10T04:30:57.247924Z'
---
