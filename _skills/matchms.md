---
id: matchms
slug: matchms
name: Matchms
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: matchms\ndescription: Spectral similarity and compound\
  \ identification for metabolomics. Use for comparing mass spectra, computing similarity\
  \ scores (cosine, modified cosine), and identifying unknown compounds from spectral\
  \ libraries. Best for metabolite identification, spectral matching, library searching.\
  \ For full LC-MS/MS proteomics pipelines use pyopenms.\nlicense: Apache-2.0 license\n\
  metadata:\n    skill-author: K-Dense Inc.\n---\n\n# Matchms\n\n## Overview\n\nMatchms\
  \ is an open-source Python..."
full_prompt_length: 7829
tools_mentioned:
- go
- Python
- python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/matchms/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/matchms/SKILL.md
fetched_at: '2026-01-25T03:51:37.268092+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:33:26.103530Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured, with a professional
      metadata header and logical organization by core capabilities. It provides specific
      code examples for each major function and references external documentation
      for deeper details. However, it lacks explicit edge case handling (e.g., what
      to do with empty spectra or incompatible formats) and doesn't define constraints
      like memory limitations for large datasets.
  usefulness:
    score: 5.0
    reasoning: This is a highly practical and valuable skill for metabolomics researchers,
      providing immediate, actionable code for common tasks like spectral comparison
      and library searching. It covers the essential workflow comprehensively from
      data import to similarity calculation, with clear guidance on when to use different
      algorithms. The inclusion of specific file formats and similarity metrics makes
      it directly applicable to real-world LC-MS/MS data analysis pipelines.
  overall_rating: 4.75
  summary: An excellent, production-ready prompt that provides comprehensive coverage
    of a specialized scientific tool with clear examples and logical structure, though
    it could benefit from more explicit error handling guidance.
  tags_suggested:
  - metabolomics
  - mass-spectrometry
  - spectral-analysis
  - scientific-computing
  - bioinformatics
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-25T04:05:51.944983Z'
indexed_at: '2026-01-25T04:05:51.944989Z'
---
