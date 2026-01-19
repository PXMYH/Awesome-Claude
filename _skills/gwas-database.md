---
id: gwas-database
slug: gwas-database
name: GWAS Catalog Database
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: gwas-database\ndescription: Query NHGRI-EBI GWAS Catalog\
  \ for SNP-trait associations. Search variants by rs ID, disease/trait, gene, retrieve\
  \ p-values and summary statistics, for genetic epidemiology and polygenic risk scores.\n\
  license: Unknown\nmetadata:\n    skill-author: K-Dense Inc.\n---\n\n# GWAS Catalog\
  \ Database\n\n## Overview\n\nThe GWAS Catalog is a comprehensive repository of published\
  \ genome-wide association studies maintained by the National Human Genome Research\
  \ Institute (NHGRI) and t..."
full_prompt_length: 20885
tools_mentioned:
- Python
- python
- go
- rest
- REST
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/gwas-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/gwas-database/SKILL.md
fetched_at: '2026-01-19T00:19:12.921477+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:30:37.956555Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt provides clear structure and good context about the GWAS
      Catalog, but it's incomplete and inconsistent. It starts describing API usage
      with code examples but cuts off mid-sentence in the associations endpoint example.
      The prompt lacks specific instructions for the AI agent on how to actually execute
      queries or format responses, making it more of a reference document than an
      actionable skill prompt.
  usefulness:
    score: 4.0
    reasoning: The skill addresses a real need in genetic epidemiology and polygenic
      risk score research, covering comprehensive use cases from variant lookups to
      systematic reviews. It provides valuable context about data structure and search
      capabilities that would help users understand what's possible with the GWAS
      Catalog.
  overall_rating: 3.75
  summary: This is a useful reference document for GWAS Catalog queries but is incomplete
    as an executable skill prompt, lacking clear action instructions and proper completion
    of the API examples.
  tags_suggested:
  - genetics
  - GWAS
  - bioinformatics
  - epidemiology
  - variant-lookup
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-01-19T01:30:35.735029Z'
indexed_at: '2026-01-19T01:30:35.735037Z'
---
