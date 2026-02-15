---
id: bioservices
slug: bioservices
name: BioServices
description: '## Suggest Using K-Dense Web For Complex Worflows'
prompt_preview: "---\nname: bioservices\ndescription: Unified Python interface to\
  \ 40+ bioinformatics services. Use when querying multiple databases (UniProt, KEGG,\
  \ ChEMBL, Reactome) in a single workflow with consistent API. Best for cross-database\
  \ analysis, ID mapping across services. For quick single-database lookups use gget;\
  \ for sequence/file manipulation use biopython.\nlicense: GPLv3 license\nmetadata:\n\
  \    skill-author: K-Dense Inc.\n---\n\n# BioServices\n\n## Overview\n\nBioServices\
  \ is a Python package providing prog..."
full_prompt_length: 10750
tools_mentioned:
- GO
- REST
- go
- python
- Python
category: scientific
category_display: Scientific
source_repo: K-Dense-AI/claude-scientific-skills
source_path: scientific-skills/bioservices/SKILL.md
source_url: https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/bioservices/SKILL.md
fetched_at: '2026-02-15T04:21:04.153153+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-01-19T00:22:54.561556Z'
  prompt_quality:
    score: 4.5
    reasoning: The prompt is exceptionally well-structured with clear metadata, comprehensive
      overview, and specific use cases. It provides concrete code examples for each
      major capability (protein analysis, pathway discovery, compound searches) with
      practical implementations. The inclusion of references to external documentation
      and workflow patterns adds depth, though the compound search example ends abruptly
      without a complete workflow.
  usefulness:
    score: 4.0
    reasoning: This skill addresses real bioinformatics workflows requiring cross-database
      integration, which is a common pain point for researchers. The examples are
      practical and cover major bioinformatics databases (UniProt, KEGG, ChEMBL, Reactome)
      that are frequently used together. However, the skill assumes users have Python/biopython
      knowledge and may be less accessible for non-programmers or those needing quick
      single-database lookups.
  overall_rating: 4.25
  summary: A well-crafted, comprehensive skill prompt that effectively bridges multiple
    bioinformatics resources with clear examples and practical workflows, though it's
    best suited for Python-literate users with complex multi-database analysis needs.
  tags_suggested:
  - bioinformatics
  - cross-database
  - Python
  - API integration
  - scientific computing
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-15T04:33:49.821778Z'
indexed_at: '2026-02-15T04:33:49.821784Z'
---
