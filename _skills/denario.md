---
id: denario
slug: denario
name: Denario
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: '---

  name: denario

  description: Multiagent AI system for scientific research assistance that automates
  research workflows from data analysis to publication. This skill should be used
  when generating research ideas from datasets, developing research methodologies,
  executing computational experiments, performing literature searches, or generating
  publication-ready papers in LaTeX format. Supports end-to-end research pipelines
  with customizable agent orchestration.

  license: GPL-3.0 license

  metadata:...'
full_prompt_length: 6819
tools_mentioned:
- go
- python
- Python
- Docker
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/denario/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/denario/SKILL.md
fetched_at: '2026-02-01T04:28:19.897352+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:26:34.456885Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt provides clear structure and good workflow documentation,
      but contains critical omissions that severely limit its practical utility. The
      installation instructions reference non-existent documentation files and the
      code examples are incomplete, which creates ambiguity about actual implementation.
      While the multi-stage research pipeline is well-conceptualized, the lack of
      concrete agent specifications and error handling guidance reduces clarity.
  usefulness:
    score: 2.5
    reasoning: The concept of automated research workflows is highly valuable for
      scientific productivity, but the prompt is fundamentally incomplete and likely
      non-functional as described. Critical dependencies on AG2/LangGraph frameworks
      are mentioned without implementation details, and the incomplete code examples
      prevent immediate use. The workflow automation from data to publication is ambitious
      but the lack of executable specifications makes practical adoption difficult
      without significant additional development.
  overall_rating: 3.0
  summary: A promising concept for scientific research automation with well-structured
    workflow documentation, but severely hampered by incomplete implementation details,
    missing dependencies, and non-functional code examples that prevent practical
    evaluation or deployment.
  tags_suggested:
  - scientific-research
  - multiagent-system
  - workflow-automation
  - latex-generation
  - research-pipeline
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:49.724047Z'
indexed_at: '2026-02-01T04:32:49.724053Z'
---
