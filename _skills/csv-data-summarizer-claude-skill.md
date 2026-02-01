---
id: csv-data-summarizer-claude-skill
slug: csv-data-summarizer-claude-skill
name: CSV Data Summarizer
description: '- Automatically detects date columns (columns containing ''date'' in
  name)'
prompt_preview: "---\nname: csv-data-summarizer\ndescription: Analyzes CSV files,\
  \ generates summary stats, and plots quick visualizations using Python and pandas.\n\
  metadata:\n  version: 2.1.0\n  dependencies: python>=3.8, pandas>=2.0.0, matplotlib>=3.7.0,\
  \ seaborn>=0.12.0\n---\n\n# CSV Data Summarizer\n\nThis Skill analyzes CSV files\
  \ and provides comprehensive summaries with statistical insights and visualizations.\n\
  \n## When to Use This Skill\n\nClaude should use this Skill whenever the user:\n\
  - Uploads or references a CSV fil..."
full_prompt_length: 5667
tools_mentioned:
- python
- Python
category: data-analytics
category_display: Data Analytics
source_repo: coffeefuelbump/csv-data-summarizer-claude-skill
source_path: SKILL.md
source_url: https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill/blob/main/SKILL.md
fetched_at: '2026-02-01T04:29:13.223377+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T01:16:28.991774Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and specific, with strong emphasis
      on immediate action and avoiding user questions. It provides excellent guidance
      on data type detection and adaptive analysis. However, it lacks explicit error
      handling for malformed CSVs or missing dependencies, and the 'How It Works'
      section is empty, which could be improved.
  usefulness:
    score: 5.0
    reasoning: This skill provides immediate, comprehensive value for anyone working
      with CSV data. It eliminates the need for manual analysis setup and automatically
      generates relevant insights and visualizations. The adaptive approach based
      on data type detection makes it highly practical across diverse real-world scenarios.
  overall_rating: 4.75
  summary: An excellent, production-ready skill that excels at automatic CSV analysis
    with strong behavioral guardrails, though it could benefit from more explicit
    error handling documentation.
  tags_suggested:
  - data-analysis
  - csv-processing
  - automated-insights
  - pandas
  - visualization
  - data-science
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:50.612594Z'
indexed_at: '2026-02-01T04:32:50.612600Z'
---
