---
id: reactome-database
slug: reactome-database
name: Reactome Database
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: reactome-database\ndescription: Query Reactome REST API\
  \ for pathway analysis, enrichment, gene-pathway mapping, disease pathways, molecular\
  \ interactions, expression analysis, for systems biology studies.\nlicense: Unknown\n\
  metadata:\n    skill-author: K-Dense Inc.\n---\n\n# Reactome Database\n\n## Overview\n\
  \nReactome is a free, open-source, curated pathway database with 2,825+ human pathways.\
  \ Query biological pathways, perform overrepresentation and expression analysis,\
  \ map genes to pathways, ex..."
full_prompt_length: 8655
tools_mentioned:
- go
- Python
- python
- REST
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/reactome-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/reactome-database/SKILL.md
fetched_at: '2026-01-25T03:51:42.637902+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:41:04.269891Z'
  prompt_quality:
    score: 2.0
    reasoning: The prompt has significant quality issues. It is incomplete, with the
      critical API call example abruptly cut off mid-sentence. The prompt also contains
      a broken reference to an internal file path ('references/api_reference.md')
      that cannot be resolved by the user, and the Python package version is outdated
      (2021), which may lead to compatibility issues.
  usefulness:
    score: 3.0
    reasoning: Despite the quality flaws, the prompt provides a useful high-level
      overview of Reactome's capabilities and the distinction between Content and
      Analysis services. The inclusion of specific API endpoints and basic code snippets
      offers a starting point for users familiar with REST APIs, though the incomplete
      example limits immediate actionability.
  overall_rating: 2.5
  summary: This is a conceptually useful but technically flawed prompt that suffers
    from critical truncation errors and outdated references, requiring significant
    user intervention to be functional.
  tags_suggested:
  - Scientific
  - Bioinformatics
  - Pathway Analysis
  - Incomplete
  - Outdated
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-25T04:05:52.102695Z'
indexed_at: '2026-01-25T04:05:52.102700Z'
---
