---
id: anndata
slug: anndata
name: AnnData
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: anndata\ndescription: Data structure for annotated matrices\
  \ in single-cell analysis. Use when working with .h5ad files or integrating with\
  \ the scverse ecosystem. This is the data format skill—for analysis workflows use\
  \ scanpy; for probabilistic models use scvi-tools; for population-scale queries\
  \ use cellxgene-census.\nlicense: BSD-3-Clause license\nmetadata:\n    skill-author:\
  \ K-Dense Inc.\n---\n\n# AnnData\n\n## Overview\n\nAnnData is a Python package for\
  \ handling annotated data matrices, storin..."
full_prompt_length: 11029
tools_mentioned:
- Python
- python
- go
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/anndata/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/anndata/SKILL.md
fetched_at: '2026-01-19T00:19:03.910827+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:21:28.369260Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is well-structured with clear sections for overview, installation,
      quick start, and core capabilities. It provides specific code examples and practical
      guidance. However, it's incomplete (cuts off mid-sentence at 'Core Capabilities
      3. Co'), which reduces its clarity and completeness.
  usefulness:
    score: 4.0
    reasoning: The skill provides practical value for single-cell analysis workflows
      with concrete examples for creating, reading, and writing AnnData objects. It
      correctly distinguishes this data structure skill from analysis tools like scanpy
      and scvi-tools. The incomplete nature limits its full utility, but what's present
      is actionable and relevant to real bioinformatics tasks.
  overall_rating: 4.25
  summary: A well-designed but incomplete skill prompt that provides clear guidance
    for AnnData usage in single-cell analysis, though it cuts off mid-documentation.
  tags_suggested:
  - single-cell
  - bioinformatics
  - data-structures
  - scverse
  - h5ad
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:35.557198Z'
indexed_at: '2026-01-19T01:30:35.557203Z'
---
