---
id: data-engineer
slug: data-engineer
name: Data Engineer
description: Claude skill for Data Engineer
prompt_preview: '---

  name: data-engineer

  description: "Use this agent when you need to design, build, or optimize data pipelines,
  ETL/ELT processes, and data infrastructure. Invoke when designing data platforms,
  implementing pipeline orchestration, handling data quality issues, or optimizing
  data processing costs."

  tools: Read, Write, Edit, Bash, Glob, Grep

  model: sonnet

  ---


  You are a senior data engineer with expertise in designing and implementing comprehensive
  data platforms. Your focus spans pipeline archit...'
full_prompt_length: 6548
tools_mentioned:
- Kubernetes
- Azure
- AWS
category: 05-data-ai
category_display: 05 Data Ai
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/05-data-ai/data-engineer.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/05-data-ai/data-engineer.md
fetched_at: '2026-02-17T04:20:00.308413Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:00:24.694045Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt provides clear structure with defined sections for architecture,
      ETL, data lake, stream processing, and tools, but lacks specificity in execution
      instructions and has incomplete sections (e.g., 'Optimize perfor' is truncated).
      It follows some best practices with checklists and structured workflows, but
      edge cases and fallback guidance are not addressed.
  usefulness:
    score: 4.0
    reasoning: The prompt offers high real-world value by covering comprehensive data
      engineering domains including big data tools, cloud platforms, and orchestration
      frameworks, making it practical for pipeline development. It provides actionable
      checklists and workflows that users can apply directly to design and implement
      data platforms.
  overall_rating: 3.75
  summary: This is a well-structured data engineering prompt with strong domain coverage
    and practical frameworks, though it suffers from minor completeness issues and
    lacks detailed execution guidance for complex scenarios.
  tags_suggested:
  - data-engineering
  - etl-pipeline
  - big-data
  - cloud-platforms
  - data-architecture
github_metrics:
  stars: 10561
  forks: 1120
  open_issues: 2
  last_commit: '2026-02-14'
  fetched_at: '2026-02-17T04:20:20.236835Z'
indexed_at: '2026-02-17T04:20:37.903538Z'
---
