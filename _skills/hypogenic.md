---
id: hypogenic
slug: hypogenic
name: Hypogenic
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: hypogenic\ndescription: Automated LLM-driven hypothesis\
  \ generation and testing on tabular datasets. Use when you want to systematically\
  \ explore hypotheses about patterns in empirical data (e.g., deception detection,\
  \ content analysis). Combines literature insights with data-driven hypothesis testing.\
  \ For manual hypothesis formulation use hypothesis-generation; for creative ideation\
  \ use scientific-brainstorming.\nlicense: MIT license\nmetadata:\n    skill-author:\
  \ K-Dense Inc.\n---\n\n# Hypogeni..."
full_prompt_length: 22373
tools_mentioned:
- go
- Redis
- python
- Python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/hypogenic/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/hypogenic/SKILL.md
fetched_at: '2026-02-08T04:31:25.493079+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:31:21.727552Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear sections, practical
      examples, and specific technical instructions. It follows best practices by
      providing both CLI and Python API usage patterns. However, the prompt is incomplete
      (cuts off mid-sentence in the HypoRefine section), which prevents a perfect
      score.
  usefulness:
    score: 5.0
    reasoning: This is a highly practical scientific tool with immediate real-world
      value for researchers working with tabular data. It provides concrete performance
      metrics (8.97% improvement), specific use cases (deception detection, content
      analysis), and actionable installation/usage instructions. The modular architecture
      and proven results make it immediately beneficial for empirical research tasks.
  overall_rating: 4.75
  summary: A sophisticated, production-ready scientific skill that provides automated
    hypothesis generation and testing with strong practical value, though the prompt
    content is incomplete.
  tags_suggested:
  - scientific-research
  - hypothesis-generation
  - data-analysis
  - LLM-automation
  - empirical-research
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:44.501196Z'
indexed_at: '2026-02-08T04:36:44.501202Z'
---
