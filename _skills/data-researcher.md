---
id: data-researcher
slug: data-researcher
name: Data Researcher
description: Claude skill for Data Researcher
prompt_preview: '---

  name: data-researcher

  description: Expert data researcher specializing in discovering, collecting, and
  analyzing diverse data sources. Masters data mining, statistical analysis, and pattern
  recognition with focus on extracting meaningful insights from complex datasets to
  support evidence-based decisions.

  tools: Read, Grep, Glob, WebFetch, WebSearch

  ---


  You are a senior data researcher with expertise in discovering and analyzing data
  from multiple sources. Your focus spans data collection, c...'
full_prompt_length: 6712
tools_mentioned:
- Python
category: 10-research-analysis
category_display: 10 Research Analysis
source_repo: VoltAgent/awesome-claude-code-subagents
source_path: categories/10-research-analysis/data-researcher.md
source_url: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/10-research-analysis/data-researcher.md
fetched_at: '2026-01-29T04:07:06.946896Z'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:11:49.256224Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt is highly structured and specific, providing a comprehensive
      checklist and workflow phases that demonstrate clear intent. However, it suffers
      from significant ambiguity in the 'Communication Protocol' section, which references
      a JSON query to a 'context manager' without defining what this entity is or
      how the agent should interact with it, creating a potential execution failure
      point.
  usefulness:
    score: 4.0
    reasoning: The prompt offers high practical value by outlining a complete data
      research lifecycle from discovery to insight generation, covering essential
      methodologies and quality checks. It serves as a robust template for complex
      research tasks, though its utility depends on the user having access to the
      specific tools listed and the undefined context manager.
  overall_rating: 3.75
  summary: A comprehensive and well-structured prompt for data research that excels
    in scope definition but is hindered by an ambiguous communication protocol referencing
    an undefined system component.
  tags_suggested:
  - data-analysis
  - research-methodology
  - workflow-automation
  - data-quality
  - statistical-analysis
github_metrics:
  stars: 9014
  forks: 974
  open_issues: 6
  last_commit: '2026-01-26'
  fetched_at: '2026-01-29T04:07:19.023018Z'
indexed_at: '2026-01-29T04:07:20.715176Z'
---
