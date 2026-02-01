---
id: geniml
slug: geniml
name: 'Geniml: Genomic Interval Machine Learning'
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: geniml\ndescription: This skill should be used when working\
  \ with genomic interval data (BED files) for machine learning tasks. Use for training\
  \ region embeddings (Region2Vec, BEDspace), single-cell ATAC-seq analysis (scEmbed),\
  \ building consensus peaks (universes), or any ML-based analysis of genomic regions.\
  \ Applies to BED file collections, scATAC-seq data, chromatin accessibility datasets,\
  \ and region-based genomic feature learning.\nlicense: BSD-2-Clause license\nmetadata:\n\
  \    skill-auth..."
full_prompt_length: 10907
tools_mentioned:
- go
- python
- Python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/geniml/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/geniml/SKILL.md
fetched_at: '2026-02-01T04:28:22.855100+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:29:09.113404Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally clear and well-structured, with a logical
      flow from overview to specific capabilities. It provides specific installation
      commands and clearly defines the scope of each module. However, it lacks explicit
      handling of edge cases (e.g., what to do if a user lacks a universe reference)
      and doesn't provide fallback guidance for common errors like missing dependencies
      or invalid BED formats.
  usefulness:
    score: 5.0
    reasoning: This is highly practical for bioinformaticians and computational biologists
      working with genomic intervals. It covers real-world workflows like single-cell
      ATAC-seq analysis and consensus peak building with specific, actionable methods.
      The reference to external documentation files allows for immediate implementation
      while maintaining a clean, focused core prompt.
  overall_rating: 4.75
  summary: A well-crafted, highly specific prompt that effectively guides users through
    complex genomic ML tasks, though it could benefit from more explicit error handling
    and edge case guidance.
  tags_suggested:
  - bioinformatics
  - genomics
  - machine-learning
  - single-cell
  - BED-files
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-01T04:32:49.773160Z'
indexed_at: '2026-02-01T04:32:49.773166Z'
---
