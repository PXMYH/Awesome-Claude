---
id: scientific-visualization
slug: scientific-visualization
name: Scientific Visualization
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: scientific-visualization\ndescription: Meta-skill for\
  \ publication-ready figures. Use when creating journal submission figures requiring\
  \ multi-panel layouts, significance annotations, error bars, colorblind-safe palettes,\
  \ and specific journal formatting (Nature, Science, Cell). Orchestrates matplotlib/seaborn/plotly\
  \ with publication styles. For quick exploration use seaborn or plotly directly.\n\
  license: MIT license\nmetadata:\n    skill-author: K-Dense Inc.\n---\n\n# Scientific\
  \ Visualization..."
full_prompt_length: 26341
tools_mentioned:
- Python
- python
- go
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/scientific-visualization/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/scientific-visualization/SKILL.md
fetched_at: '2026-01-19T00:19:24.708177+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:43:03.379042Z'
  prompt_quality:
    score: 4.0
    reasoning: The prompt is well-structured with clear sections and practical code
      examples, but it references external assets (style_presets.py, figure_export.py,
      assets/) that aren't defined in the prompt itself. This creates ambiguity about
      implementation details and dependencies, though the core guidance is specific
      and actionable.
  usefulness:
    score: 4.5
    reasoning: Highly practical for scientific researchers needing publication-ready
      figures, with comprehensive coverage of journal-specific requirements, accessibility
      considerations, and export formats. The multi-tool orchestration (matplotlib/seaborn/plotly)
      and real-world examples make it immediately applicable for manuscript preparation.
  overall_rating: 4.25
  summary: A strong, practical skill for scientific visualization that provides clear
    guidance for publication-quality figures, though it could be improved by including
    the referenced helper functions directly rather than assuming external dependencies.
  tags_suggested:
  - scientific-visualization
  - publication-figures
  - matplotlib
  - seaborn
  - plotly
  - data-visualization
  - research-tools
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:36.002025Z'
indexed_at: '2026-01-19T01:30:36.002030Z'
---
