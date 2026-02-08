---
id: geo-database
slug: geo-database
name: GEO Database
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: geo-database\ndescription: Access NCBI GEO for gene expression/genomics\
  \ data. Search/download microarray and RNA-seq datasets (GSE, GSM, GPL), retrieve\
  \ SOFT/Matrix files, for transcriptomics and expression analysis.\nlicense: Unknown\n\
  metadata:\n    skill-author: K-Dense Inc.\n---\n\n# GEO Database\n\n## Overview\n\
  \nThe Gene Expression Omnibus (GEO) is NCBI's public repository for high-throughput\
  \ gene expression and functional genomics data. GEO contains over 264,000 studies\
  \ with more than 8 mill..."
full_prompt_length: 25348
tools_mentioned:
- go
- python
- Python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/geo-database/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/geo-database/SKILL.md
fetched_at: '2026-02-08T04:31:24.232121+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:29:27.360887Z'
  prompt_quality:
    score: 3.5
    reasoning: The prompt provides clear explanations of GEO data structures and includes
      functional Python code examples, but it's incomplete and lacks critical elements.
      The advanced search section cuts off mid-sentence, and there's no guidance on
      error handling, authentication requirements, or rate limiting. It also doesn't
      specify how the skill should be invoked or what the expected output format is.
  usefulness:
    score: 4.0
    reasoning: The skill addresses a genuine need for accessing GEO data, which is
      essential for bioinformatics and transcriptomics research. The code examples
      are practical and demonstrate real-world usage patterns for searching and retrieving
      data. However, the incomplete nature and lack of download functionality for
      actual data files (SOFT/Matrix) limits its immediate utility.
  overall_rating: 3.75
  summary: This is a partially developed skill with valuable conceptual explanations
    and working code snippets for searching GEO, but it's incomplete and lacks critical
    functionality for actual data retrieval and error handling.
  tags_suggested:
  - bioinformatics
  - gene-expression
  - NCBI
  - transcriptomics
  - data-retrieval
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-08T04:36:44.471048Z'
indexed_at: '2026-02-08T04:36:44.471053Z'
---
